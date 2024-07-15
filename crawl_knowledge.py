import os
import requests
from bs4 import BeautifulSoup
import html2text
from dotenv import load_dotenv

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

def crawl_and_convert_to_markdown(url, remove_table=True):
    
    # BS4
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    if remove_table:
        for table in soup.find_all('table'):
            table.decompose()

    article = soup.find('article') 

    # convert to markdown
    if article:
        md_converter = html2text.HTML2Text()
        md_converter.body_width = 0  # Disable wrapping
        markdown_content = md_converter.handle(str(article))

        print(markdown_content)

        return markdown_content
    else:
        return None
    

def tokenizer(model_id, input):

    # generate token
    authenticator = IAMAuthenticator(os.environ["API_KEY"])
    access_token = authenticator.token_manager.get_token()

    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/tokenization?version=2023-05-29"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }

    body = {
        "input": input,
        "model_id": model_id,
        "project_id": os.environ["PROJECT_ID"]
    }

    response = requests.post(
        url = url,
        headers=headers,
        json=body
    )

    print(response.content)


def craw_knowledge(url, save_file=True):
    md = crawl_and_convert_to_markdown(url)
    tokenizer(model_id="ibm/granite-13b-chat-v2", input=md)
    
    if save_file:
        with open("knowledge_submission/result.md", "w") as f:
            f.write(md)

    # save JSON with number of tokens

if __name__ == "__main__":

    url_monitors = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=models-configuring-model-evaluations"
    url_quality = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-quality"
    url_fairness_metrics = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness-metrics"
    url_model_transaction = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=transactions-explaining-model"

    craw_knowledge(url_monitors, save_file=False)
