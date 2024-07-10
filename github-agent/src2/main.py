import os
from crewai import Agent, Task, Crew, Process
from gh_tool import GitHubAPITool  # Make sure to import the GitHubAPITool class

# Define tools
github_tool = GitHubAPITool()

# Define agents
issue_finder = Agent(
    role='Issue Finder',
    goal='Find issues labeled "xyz" in the GitHub repository.',
    backstory='You are an adept issue tracker, capable of quickly finding issues that match specific criteria.',
    tools=[github_tool]
)

code_extractor = Agent(
    role='Code Extractor',
    goal='Review the identified issue and extract the relevant code.',
    backstory='You are proficient in navigating codebases and extracting relevant code for given issues.',
    tools=[github_tool]
)

developer = Agent(
    role='Developer',
    goal='Write tests and code to solve the identified issue.',
    backstory='You are a skilled developer who can write effective tests and code solutions for various issues.',
    tools=[github_tool]
)

pr_manager = Agent(
    role='PR Manager',
    goal='Manage the pull request process.',
    backstory='You ensure that code changes are properly reviewed and integrated into the repository.',
    tools=[github_tool]
)

# Define tasks
find_issue_task = Task(
    description='Find issues labeled "xyz" in the GitHub repository.',
    expected_output='A list of issues with relevant details.',
    tools=[github_tool],
    agent=issue_finder,
    run=lambda inputs: github_tool.find_issues(inputs['repository'], 'xyz')
)

extract_code_task = Task(
    description='Review the identified issue and extract the relevant code.',
    expected_output='Extracted code snippets related to the issue.',
    tools=[github_tool],
    agent=code_extractor,
    run=lambda inputs: github_tool.get_code(inputs['repository'], 'path/to/code')
)

write_tests_and_code_task = Task(
    description='Write tests and code to solve the identified issue.',
    expected_output='Tests and code committed to a new branch.',
    tools=[github_tool],
    agent=developer,
    run=lambda inputs: github_tool.commit_code(inputs['repository'], 'path/to/code', 'branch', 'Commit message', 'encoded content')
)

create_pr_task = Task(
    description='Manage the pull request process.',
    expected_output='A pull request created if tests pass; otherwise, iterate on the code until tests pass.',
    tools=[github_tool],
    agent=pr_manager,
    run=lambda inputs: github_tool.create_pr(inputs['repository'], 'PR Title', 'head-branch', 'base-branch')
)

# Form the crew
crew = Crew(
    agents=[issue_finder, code_extractor, developer, pr_manager],
    tasks=[find_issue_task, extract_code_task, write_tests_and_code_task, create_pr_task],
    process=Process.sequential
)

# Kickoff the crew with the repository details
result = crew.kickoff(inputs={'repository': 'owner/repo_name'})
print(result)
