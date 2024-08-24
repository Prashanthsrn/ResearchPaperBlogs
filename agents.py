from crewai import Agent
from dotenv import load_dotenv
from tools import search_tool,websearch_tool

load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose = True,
    temperature=0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY"))

## Researcher Agent 
researcher = Agent(
    role = "Senior paper researcher",
    goal = "Read through 5 latest and most relevant research papers in the topic {topic} and gets information from it",
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curiosity, at the forefront of all the tech related research papers. Eager researcher eploring papers that can change the world"
    ),
    tool = [search_tool,websearch_tool],
    allow_delegation = True,
    llm = llm
)


## Blog Writer
writer = Agent(
    role = "Writer",
    goal = "Narrate compelling summaries on the topic {topic}. Writes further possible research areas in the topic {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplyfying complex topics into a summary. Makes engaging narrative that captivate and educate, bringing new discoveries and technologies to light."
    ),
    tools = [search_tool,websearch_tool],
    llm = llm,
    allow_delegation = False
)