import os
import shutil
import subprocess
import tempfile
from crewai_tools import tool, RagTool

# Tool decorator for GitHub Pull Request Creator
@tool("GitHub Pull Request Creator")
def create_pull_request(repo_name: str, branch_name: str, title: str, body: str) -> str:
    """
    Create a GitHub pull request using `gh` CLI tool.

    Parameters:
    - repo_name: Name of the GitHub repository.
    - branch_name: Name of the branch to create the pull request from.
    - title: Title of the pull request.
    - body: Body or description of the pull request.

    Returns:
    - URL of the created pull request.
    """
    try:
        # Clone repository into a temporary directory
        temp_dir = tempfile.mkdtemp()
        repo_dir = os.path.join(temp_dir, repo_name.split('/')[-1].replace('.git', ''))
        clone_command = f"git clone {repo_name} {repo_dir}"
        subprocess.run(clone_command, shell=True, check=True)

        # Initialize RagTool for file operations
        rag_tool = RagTool()

        # Read file contents using RagTool (example reading README.md)
        readme_path = os.path.join(repo_dir, 'README.md')
        readme_content = rag_tool.read_file(readme_path)

        # Modify README content (example: append a new section)
        new_readme_content = readme_content + f"\n\n## New Section\n{body}"

        # Write modified README content back to the file
        rag_tool.write_file(readme_path, new_readme_content)

        # Stage changes and commit in the cloned repository
        subprocess.run(f"cd {repo_dir} && git add .", shell=True, check=True)
        subprocess.run(f"cd {repo_dir} && git commit -m 'Update README with new section'", shell=True, check=True)

        # Push changes to the remote branch
        push_command = f"cd {repo_dir} && git push origin {branch_name}"
        subprocess.run(push_command, shell=True, check=True)

        # Create pull request using `gh` CLI tool
        pr_command = f"gh pr create --repo {repo_name} --head {branch_name} --title '{title}' --body '{body}'"
        result = subprocess.run(pr_command, shell=True, check=True, capture_output=True, text=True)
        pr_url = result.stdout.strip()

        return pr_url

    except subprocess.CalledProcessError as e:
        # Handle errors if any subprocess command fails
        return f"Error creating pull request: {e}"

    finally:
        # Clean up temporary directory
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
