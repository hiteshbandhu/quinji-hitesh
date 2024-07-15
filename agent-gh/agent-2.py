from crewai import Crew, Agent, Task
from crewai_tools import GithubSearchTool
import os

repo = "hiteshbandhu/notes-ai-and-tech"
level = "beginner"

gh_tool = GithubSearchTool(github_repo="hiteshbandhu/notes-ai-and-tech", content_types = ['issue'], gh_token = os.getenv("GH_TOKEN"))

agent = Agent(
  role='Issue Finder',
  goal='Find issues in a github repo, based on the detailed given',
  backstory="""You're a product manager at microsoft, who is good at finding and giving out tasks to coder in your team. You see issues in the repo and are known to be excellent at giving to the coder with the same skills to solve it. You are considered a five star employee""",
  verbose=True
)

task = Task(
  description=f'Find issues from the issues tab in a github repo, regarding frontend',
  expected_output="A github issue and its details and body, and what is expected to be done",
  agent=agent,
  tools=[gh_tool]
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=10
)

result = crew.kickoff()
print(result)