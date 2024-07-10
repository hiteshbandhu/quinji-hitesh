from dotenv import load_dotenv
from crewai import Crew, Task
from agents import pr_creator_agent, github_search_tool
from tools import create_pull_request
import os

load_dotenv()

# Input parameters (replace with actual values or input prompts)
repo_url = os.getenv("REPO_URL")
branch_name = "main"
title = "Automated PR Title"
body = "Automated PR Body"

# Create Agents
pr_agent = pr_creator_agent()

# Create Tasks
def pr_task(agent, repo_url, branch_name, title, body):
    return Task(
        description='Search and modify the README file, and create a pull request',
        expected_output='URL of the created pull request',
        agent=agent,
        tools=[
            github_search_tool(repo_url),
            create_pull_request(repo_url, branch_name, title, body)
        ],
        inputs={
            "repo_url": repo_url,
            "branch_name": branch_name,
            "title": title,
            "body": body
        }
    )

# Create Crew
crew = Crew(
    agents=[pr_agent],
    tasks=[pr_task(agent=pr_agent, repo_url=repo_url, branch_name=branch_name, title=title, body=body)],
    verbose=2
)

# Kickoff the crew
result = crew.kickoff({
    "repo_url": repo_url,
    "branch_name": branch_name,
    "title": title,
    "body": body
})

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)
