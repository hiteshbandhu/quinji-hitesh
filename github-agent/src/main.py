from agents import *
from tools import *
from tasks import *
from crewai import Process, Crew

crew = Crew(
    agents=[issue_finder, coder],
    tasks=[issue_task, code_task],
    process=Process.sequential,
    verbose=7,
)

result = crew.kickoff()
print(result)




