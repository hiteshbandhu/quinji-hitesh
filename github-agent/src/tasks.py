from crewai import Task
from tools import *
from agents import  *

issue_task = Task(
  description='Find the best issue in the github respository that can be solved easily and is easy for intermediate',
  expected_output='A github issue with full description and details',
  agent=issue_finder,
  tools=[gh_tool]
)

code_task = Task(
  description='Solve the given issue to you and spit out the code at the end',
  expected_output='Code in Markdown blocks with full comments',
  agent=coder,
)



