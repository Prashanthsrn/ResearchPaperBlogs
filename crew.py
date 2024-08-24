from crewai import Crew, Process
from tasks import research_task,writing_task
from agents import researcher,writer


crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task,writing_task],
    process=Process.sequential,
)

## excecute task
result = crew.kickoff(inputs={'topic':'AI in gaming'})
print(result)