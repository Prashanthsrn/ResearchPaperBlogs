from crewai import Task
from agents import researcher, writer
from tools import search_tool,websearch_tool

## research task
research_task = Task(
    description = (
        "Identify 5 top, recent and relevant papers in the topic {topic}"
        "Focus on what the paper wants to convey, and what new research was done in this paper"
        "Your final report should be a clear summary of each paper with its name, author, date of publication,"
        "its future research oppurtunities and any real life product that uses this research, if any"
    ),
    expected_output = "In detailed 5 paragraph report on each of the research papers in the feild of AI and deeplearning",
    agent = researcher,
    tools = [search_tool,websearch_tool]
)

writing_task = Task(
    description = (
        "Compose an insightful article on the topic {topic}"
        "Focus on the latest trends and how its impacting the industry"
        "The article should be easy to read, understand, engaging and positive"
    ),
    expected_output = "Comprehensive 4 paragraph report on {topic}",
    agent = writer,
    tools = [search_tool,websearch_tool],
    output_file = "newBlog.md"
)