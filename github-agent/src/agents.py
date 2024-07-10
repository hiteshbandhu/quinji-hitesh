from crewai import Agent
from tools import *

issue_finder = Agent(
  role='Github Issue Delegator',
  goal='Find the best issue in the github respository that can be solved easily and is easy for intermediate programmers',
  backstory="""Use the GithubSearchTool. You do not see the code, you can only see the issues tab.You are very good at delegating issues to programmers who can solve them. You have a comprehensive analysis""",
  tools = [gh_tool],
  allow_delegation = False,
  verbose=True,
)



coder = Agent(
  role='Programmer',
  goal='Write quality code to solve the github issue given to you',
  backstory="""You are a very experienced programmer who likes to solve issues about github repositories. You write maintainable and good code following first principles and you know every programming language possible there. You are a talented individual """,
  allow_delegation = False,
  verbose=True,
)



