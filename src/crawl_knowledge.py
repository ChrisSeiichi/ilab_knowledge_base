import logging
import os
from time import sleep

import html2text
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from selenium import webdriver

logging.basicConfig(level=logging.INFO)

load_dotenv()


def crawl_and_convert_to_markdown(url: str, remove_table: bool = True) -> str:
    """Crawl the url and convert it to MD format.

    Args:
        url: URL with the content to crawl
        remove_table: remove any table from the content. Defaults to True.

    Returns:
        Extracted content in markdown format
    """

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    # If there is 403, use selenium
    if soup.find("div", {"class": "error-code"}):
        logging.info("Scraping with selenium... sleep 3 seconds")
        driver = webdriver.Chrome()
        sleep(5)
        driver.get(url)
        html_content = driver.page_source

        soup = BeautifulSoup(html_content, "html.parser")

    if remove_table:
        logging.info("Removing tables")
        for table in soup.find_all("table"):
            table.decompose()

    article = soup.find("article")  # article tags for IBM doc

    # Convert to markdown
    if article:
        md_converter = html2text.HTML2Text()
        md_converter.body_width = 0  # Disable wrapping
        markdown_content = md_converter.handle(str(article))

        logging.info("Converted to markdown")

        return markdown_content

    else:
        return "No article found"


def tokenizer(model_id, input):
    """Get number of token from the given string input

    Args:
        model_id: model ID from watsonx.ai
        input: string input to count
    """

    # generate token
    authenticator = IAMAuthenticator(os.environ["WX_API_KEY"])
    access_token = authenticator.token_manager.get_token()

    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/tokenization?version=2023-05-29"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(access_token),
    }

    body = {"input": input, "model_id": model_id, "project_id": os.environ["WX_PROJECT_ID"]}

    response = requests.post(url=url, headers=headers, json=body)

    logging.info(response.content)


def craw_knowledge(url: str, file_name: str):
    """Crawl knowledge base and save locally

    Args:
        url: url to crawl
        file_name: local file name to be saved
    """
    md = crawl_and_convert_to_markdown(url, remove_table=True)

    tokenizer(
        model_id="meta-llama/llama-3-1-70b-instruct", input=md
    )  # meta-llama/llama-3-1-70b-instruct #ibm/granite-13b-chat-v2

    file_path = os.path.join("knowledge_submission", file_name)
    with open(file_path, "w") as f:
        logging.info(f"Saving file locally: {file_path}")
        f.write(md)


if __name__ == "__main__":
    dataset = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=models-managing-data-model-evaluations"
    monitors = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=models-configuring-model-evaluations"
    fairness_metrics = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=evaluations-fairness"
    model_transaction = "https://www.ibm.com/docs/en/cloud-paks/cp-data/5.0.x?topic=transactions-explaining-model"
    ml_frameworks = (
        "https://www.ibm.com/docs/en/watsonx/saas?topic=models-supported-machine-learning-engines-frameworks"
    )

    list_url = [dataset, monitors, fairness_metrics, model_transaction, ml_frameworks]

    for url in list_url:
        topic = url.split("topic=")[1]
        craw_knowledge(url=url, file_name=f"result_{topic}.md")
