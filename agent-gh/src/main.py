from agents import *
from tasks import *
from crewai_tools import GithubSearchTool, FileReadTool
from crewai import Crew

from os import getenv

GH_REPO = "hiteshbandhu/notes-ai-and-tech"

domain = input("What domain of issues you want to solve (frontent, backend, docker, etc.) :>   ")

# initialising tools
issue_tool = GithubSearchTool(github_repo=GH_REPO, gh_token = getenv("GH_TOKEN"), content_types = ['issues'])
code_tool = GithubSearchTool(github_repo=GH_REPO, gh_token = getenv("GH_TOKEN"), content_types = ['code'])
file_read_tool = FileReadTool()


# importing and running the crew

crew = Crew(
    agents=[planning_agent, code_agent, qa_agent, cheif_qa],
    tasks=[review_task, code_task, evaluate_task, plan_task],
    verbose=10
)

result = crew.kickoff({"domain" : domain})

print(result)