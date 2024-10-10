import os
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from mypy_extensions import TypedDict
from typing import Annotated
import operator
from langgraph.types import Send
import json
from langgraph.graph import END, StateGraph, START

from qna_chain import qna_chain

# States
class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        md_filename: markdown filename
        context: question
        questions_and_answers: LLM generation
    """

    md_filename: str
    iterations: list
    context: str
    questions_and_answers: Annotated[list, operator.add]
    

class QnAState(TypedDict):
    context: str
    iteration: int


# Node function
def retrieve_markdown(state: GraphState):
    """
    Retrieve documents
    """
    print("---RETRIEVE---")
    md_filename = state["md_filename"]
    print(md_filename)

    # Retrieval
    loader = UnstructuredMarkdownLoader(md_filename)
    document = loader.load()
    return {"md_filename": md_filename, "context": document}


def generate_qna(state: QnAState):
    """
    Generate answer
    """
    context = state["context"]

    print("---GENERATE---")
    generation = qna_chain.invoke({"context": context})
    return {"questions_and_answers": [generation]}


def select_qna(state):
    print("---SELECT---")
    
    for qna in state["questions_and_answers"]:
        print(qna['question'])

    # Saving
    filename=state["md_filename"].split("/")[-1] # removing the file type
    # filename=filename.split("/")[-1]
    qna_dict = {"questions_and_answers": state["questions_and_answers"]}
    fp = f"yaml_construction/questions_and_answers/{filename}.json"
    with open(fp, "w") as f:
        json.dump(qna_dict, f)


# Edge functions
def continue_to_qna(state: GraphState):
    return [Send("generate_qna", {"context": state["context"], "iteration": i}) for i in state["iterations"]]


# Compile

def compile_graph():

    graph = StateGraph(GraphState)

    # Define the nodes and edges
    graph.add_edge(START, "retrieve_markdown")
    graph.add_node("retrieve_markdown", retrieve_markdown)  # markdown retriever
    graph.add_conditional_edges("retrieve_markdown", continue_to_qna ,["generate_qna"])
    graph.add_node("generate_qna", generate_qna)  # generatae
    graph.add_edge("generate_qna", "select_qna")
    graph.add_node("select_qna", select_qna)  # grade the questions
    graph.add_edge("select_qna", END)

    workflow = graph.compile()
    # workflow.get_graph().draw_mermaid_png()

    return workflow


if __name__=="__main__":

    workflow = compile_graph()

    MD_DIR = "yaml_construction/context/reduced/evaluations-fairness.md"
    # Start workflow
    i=1
    for markdown in os.listdir(MD_DIR)[:]:
        print(markdown)
        filepath = os.path.join(MD_DIR, markdown)
        while i<50: # no more than 10 tries
            try:
                print(f"---Converting {markdown}---")
                print(f"---Iteration {i}---")
                for s in workflow.stream({"md_filename": filepath, "iterations": list(range(3))}):
                    print(s)
                i=1

            except Exception as e:
                i+=1
                print(e)
                continue
            break
