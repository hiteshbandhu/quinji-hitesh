from crewai import Agent
from crewai_tools import GithubSearchTool, RagTool
from os import getenv

def pr_creator_agent():
    """
    Define an agent responsible for automating the creation of pull requests.
    """
    return Agent(
        role='PR Creator',
        goal='Search for the README.md file, make necessary changes, and create a pull request',
        backstory="""You're a developer tasked with automating the process of searching and updating the README file,
        and creating a pull request using GitHub's CLI tool.""",
        verbose=True
    )

def github_search_tool(repo_url):
    """
    Initialize the GithubSearchTool for searching code within a specific GitHub repository.
    
    Parameters:
    - repo_url: URL of the GitHub repository to search.
    """
    return GithubSearchTool(
        github_repo=repo_url,
        gh_token=getenv("GH_TOKEN"),  # Make sure to provide your GitHub token
        content_types=['code']  # Searching for code only
    )

def rag_tool():
    """
    Initialize the RAG Tool for file operations.
    """
    return RagTool()
