import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


def get_llm():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY was not found in the .env file."
        )

    # Remove accidental spaces/newlines
    api_key = api_key.strip()

    llm = ChatOpenAI(
        model="gpt-5.6-luna",
        temperature=0,
        api_key=api_key
    )

    return llm