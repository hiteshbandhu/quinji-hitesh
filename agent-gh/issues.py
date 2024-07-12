from github import Github
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Step 1: Set up your environment
GITHUB_TOKEN = os.getenv("GH_TOKEN")
USERNAME = 'nginx'
REPO_NAME = 'unit'
REPO_LINK = f"{USERNAME}/{REPO_NAME}"

# Step 2: Authenticate with GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_LINK)

# Step 3: Search issues with the 'good-first-issue' label and keyword 'python'
label_name = 'L-python'
keyword = ''
max_issues = 10
found_issues = []

# Fetch issues and filter by label and keyword
issues = repo.get_issues(state='open', labels=[label_name])

for issue in issues:
    if keyword in issue.title.lower() or keyword in issue.body.lower():
        found_issues.append(issue)

    # Stop when we've found enough issues
    if len(found_issues) >= max_issues:
        break

# Print the found issues
for issue in found_issues:
    print(f"Issue #{issue.number}: {issue.title}")






