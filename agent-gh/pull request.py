import subprocess
import shutil
import os
from github import Github
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Step 1: Set up your environment
GITHUB_TOKEN = os.getenv("GH_TOKEN")
USERNAME = 'hiteshbandhu'
REPO_NAME = 'notes-ai-and-tech'
REPO_LINK = f"{USERNAME}/{REPO_NAME}"
BRANCH_NAME = 'feature_branch'  # Create a new feature branch
BASE_BRANCH = 'master'
SOURCE_FILE_PATH = '/Users/hiteshbandhu/Developer/agent-gh/SOP.md'
DEST_FILE_PATH = 'SOP.md'  # The destination path in the cloned repo
COMMIT_MESSAGE = 'add - SOP.md'
PR_TITLE = 'Adding SOP to make this like Obsidian'
PR_BODY = 'Adding the SOP for Obsidian. Link: obsidian.md\n\nCloses #2'


#### Chapter 3 
# Directory name derived from repo name
repo_dir = REPO_NAME.split('/')[-1]

# Step 2: Clone the repository
print("Cloning the repository...")
subprocess.run(['git', 'clone', f'https://github.com/{REPO_LINK}.git'])

# Step 3: Copy the file to the cloned repository directory
print(f"Copying {SOURCE_FILE_PATH} to {repo_dir}/{DEST_FILE_PATH}...")
shutil.copy(SOURCE_FILE_PATH, os.path.join(repo_dir, DEST_FILE_PATH))

## this is a change made to test, its a test case, this will be replaced by the agent

# Step 4: Change to the repository directory
os.chdir(repo_dir)
print(f"Changed directory to {repo_dir}")

# Step 5: Create a new branch and switch to it
print(f"Creating and switching to a new branch '{BRANCH_NAME}'...")
subprocess.run(['git', 'checkout', '-b', BRANCH_NAME])

# Step 6: Add the new file
print("Adding the new file...")
subprocess.run(['git', 'add', DEST_FILE_PATH])

# Step 7: Commit the changes
print("Committing the changes...")
subprocess.run(['git', 'commit', '-m', COMMIT_MESSAGE])

# Step 8: Push the new branch to GitHub
print(f"Pushing the new branch '{BRANCH_NAME}' to GitHub...")
subprocess.run(['git', 'push', 'origin', BRANCH_NAME])

# # Verify the commit in the new branch
# print("Verifying the commit in the new branch...")
# subprocess.run(['git', 'log', '-1'])

# Step 9: Create a pull request using the GitHub API
print("Creating a pull request...")
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_LINK)

# Create the pull request
pr = repo.create_pull(
    title=PR_TITLE,
    body=PR_BODY,
    head=BRANCH_NAME,
    base=BASE_BRANCH
)

print(f'Pull request created: {pr.html_url}')
