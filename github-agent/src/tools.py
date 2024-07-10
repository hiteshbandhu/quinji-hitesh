from dotenv import load_dotenv
load_dotenv()
from os import getenv
from crewai_tools import GithubSearchTool, CodeDocsSearchTool

gh_tool = GithubSearchTool(
    gh_token = getenv("gh_token"),
    github_repo='hiteshbandhu/notes-ai-and-tech',
    content_types=['code', 'issue', 'pr'] 
)


