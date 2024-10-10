from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
import os
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


# Parser
class QuestionsandAnswers(BaseModel):
    question: str = Field(description="question related to the context")
    answer: str = Field(description="answer to the question using the context")


def define_qna_generation_chain():
    parser = JsonOutputParser(pydantic_object=QuestionsandAnswers)    

    # LLM
    template = """
    You are a robot that only outputs JSON.
    You reply in JSON format, do not introduce your answer.
    Using the provided context, create a relevant question and answer, that would help deepen someone's knowledge.

    Context:
    {context}

    {format_instructions}

    DO NOT add any comments such as */
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["context"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    parameters = {
        "decoding_method": "sample",
        "max_new_tokens": 200,
        "min_new_tokens": 10,
        "temperature": 0.5,
        "top_k": 50,
        "top_p": 1,
    }

    llm = WatsonxLLM(
        model_id="meta-llama/llama-3-1-70b-instruct",
        # model_id="meta-llama/llama-3-405b-instruct",
        url="https://us-south.ml.cloud.ibm.com",
        project_id=os.environ["WX_PROJECT_ID"],
        apikey=os.environ["WX_API_KEY"],
        params=parameters
    )

    qna_chain = prompt | llm | parser

    return qna_chain

qna_chain = define_qna_generation_chain()