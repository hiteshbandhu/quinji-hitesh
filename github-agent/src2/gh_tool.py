import os
import requests
from crewai_tools import tool

class GitHubAPITool:
    def __init__(self):
        self.api_key = os.getenv('GITHUB_API_KEY')
        self.headers = {
            'Authorization': f'token {self.api_key}',
            'Accept': 'application/vnd.github.v3+json',
        }

    def find_issues(self, repo, label):
        url = f'https://api.github.com/repos/{repo}/issues?labels={label}'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_code(self, repo, path, branch='main'):
        url = f'https://api.github.com/repos/{repo}/contents/{path}?ref={branch}'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def commit_code(self, repo, path, branch, message, content):
        url = f'https://api.github.com/repos/{repo}/contents/{path}'
        data = {
            'message': message,
            'content': content,
            'branch': branch,
        }
        response = requests.put(url, headers=self.headers, json=data)
        return response.json()

    def create_pr(self, repo, title, head, base):
        url = f'https://api.github.com/repos/{repo}/pulls'
        data = {
            'title': title,
            'head': head,
            'base': base,
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def run_tests(self, repo, workflow_id, ref='main'):
        url = f'https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/dispatches'
        data = {
            'ref': ref,
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()
