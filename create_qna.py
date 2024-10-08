import csv

import yaml


def read_csv(file_path):
    """Reads the CSV file and returns a list of questions and answers."""
    questions_and_answers = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions_and_answers.append({"question": row["question"], "answer": row["answer"]})
    return questions_and_answers


def create_yaml(context, questions_and_answers, output_file):
    """Creates a YAML file with the specified context and questions/answers."""
    data = {"seed_examples": [{"questions_and_answers": questions_and_answers}]}

    with open(output_file, "w") as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    # /!\ needs 5 contexts
    # /!\ context limit of 500 words
    # /!\ needs at least 3 qna
    # /!\ qna pair limit of 250 words
    # /!\ no markdown tables

    """
    - crawl information and create .md

    - create the qna
        - from the .md, select a context of max 500 words, and create 3 qna pairssave it in yaml with langgraph?
        - review it
        - save in yaml
    """
    qna = read_csv()
    create_yaml()
