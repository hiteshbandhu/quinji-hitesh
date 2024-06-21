from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew
from crewai_tools import PDFSearchTool

code_agent = Agent(
  role='Programmer',
  goal='Write Code to Combine all pdf files in a directory to one ',
  backstory="""You're an expert python developer specialising in handling files and processes, and you only use the provided official-python-documentation in the tools. Don't use the internet. Use descrptive comments in the code and also explain why you used this code and what it is doing""",
  verbose=True
)

tool = PDFSearchTool('library.pdf')

task = Task(
  description='Write Code to Combine all pdf files in a directory to one',
  # expected_output='Python Code to combine',
  expected_output='Python Code to combine all the files.',
  agent=code_agent,
  tools=[tool]
)

crew = Crew(
    agents=[code_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print(result)
