from crewai_tools import GithubSearchTool, FileReadTool
from os import getenv

GH_REPO = "hiteshbandhu/notes-ai-and-tech"
issue_tool = GithubSearchTool(github_repo=GH_REPO, gh_token = getenv("GH_TOKEN"), content_types = ['issue'])
code_tool = GithubSearchTool(github_repo=GH_REPO, gh_token = getenv("GH_TOKEN"), content_types = ['code'])
file_read_tool = FileReadTool()
