import os
import requests
from requests.exceptions import RequestException
from time import sleep

# GitHub API URL
API_URL = 'https://api.github.com'

# Environment variable for GitHub Personal Access Token
GITHUB_TOKEN = os.getenv('GITHUB_PAT')

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Function to make API requests with retry logic
def make_request(url, max_retries=3, backoff_factor=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f'Request failed: {e}, Attempt {attempt + 1} of {max_retries}')
            sleep(backoff_factor * (2 ** attempt))
    raise RequestException(f'Failed to fetch data after {max_retries} attempts')

# Fetch today's commits
def fetch_commits():
    url = f'{API_URL}/repos/owner/repo/commits?since={{start_of_today}}'
    commits = make_request(url)
    for commit in commits:
        print(f'Author: {commit['commit']['author']['name']}, Message: {commit['commit']['message']}')

# Count open and closed issues
def count_issues():
    open_issues = make_request(f'{API_URL}/search/issues?q=repo:owner/repo+is:issue+state:open')
    closed_issues = make_request(f'{API_URL}/search/issues?q=repo:owner/repo+is:issue+state:closed')
    print(f'Open Issues: {open_issues['total_count']}, Closed Issues: {closed_issues['total_count']}')

if __name__ == '__main__':
    fetch_commits()
    count_issues()
