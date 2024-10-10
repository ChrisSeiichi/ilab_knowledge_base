import json
import yaml
import os
from typing import List

def create_yaml_from_files(json_files: List[str], md_files: List[str], output_file: str):
    # Load questions and answers from the JSON file
    JSON_FOLDER = "yaml_construction/questions_and_answers"
    MD_FOLDER = "yaml_construction/context/reduced"

    seed_examples_list = []
    for json_file, md_file in zip(json_files, md_files):
        with open(os.path.join(JSON_FOLDER, json_file), 'r') as f:
            questions_and_answers = json.load(f)
        
        with open(os.path.join(MD_FOLDER, md_file), 'r') as f:
            context = f.read()

        seed_example = {
                    'context': context,
                    'questions_and_answers': questions_and_answers["questions_and_answers"]
                    }
    
        seed_examples_list.append(seed_example)

    # Create the YAML structure
    yaml_content = {
        'version': 3,
        'domain':"technology",
        'created_by':"christophe.martin@ibm.com",
        'seed_examples': seed_examples_list
    }
    
    # Write the structure to the output YAML file
    with open(output_file, 'w') as f:
        yaml.dump(yaml_content, f, default_flow_style=False, sort_keys=False)
    
    print(f"YAML file created: {output_file}")



if __name__ == "__main__":
    # /!\ needs 5 contexts
    # /!\ context limit of 500 words
    # /!\ needs at least 3 qna
    # /!\ qna pair limit of 250 words
    # /!\ no markdown tables

    json_list = ["part_1.md.json",
                 "part_2.md.json",
                 "part_3.md.json",
                 "part_4.md.json",
                 "part_5.md.json",
                 ]
    
    md_list = ["evaluations-fairness.md/part_1.md",
                 "evaluations-fairness.md/part_2.md",
                 "evaluations-fairness.md/part_3.md",
                 "evaluations-fairness.md/part_4.md",
                 "evaluations-fairness.md/part_5.md",
                 ]

    create_yaml_from_files(json_files=json_list, 
                           md_files=md_list, 
                           output_file='output.yaml')
