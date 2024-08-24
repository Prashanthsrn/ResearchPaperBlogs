from dotenv import load_dotenv

load_dotenv()

import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

from crewai_tools import SerperDevTool
from crewai_tools import WebsiteSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose = True,
    temperature=0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY"))


websearch_tool = WebsiteSearchTool(
    website="https://arxiv.org/",
    config={
        'llm': {
            'model': llm.model,
            'temperature': llm.temperature,
            'google_api_key': llm.google_api_key.get_secret_value()  # Extract the actual API key value
        }
    }
)

search_tool = SerperDevTool()