import os
import requests

# Securely access GitHub Personal Access Token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPO = 'https://api.github.com/repos/username/repository'

# Headers to authenticate with GitHub API using the token
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Fetch the number of commits
commits_response = requests.get(f'{GITHUB_REPO}/commits', headers=headers)
commits_data = commits_response.json()

# Fetch the number of open and closed issues
issues_response = requests.get(f'{GITHUB_REPO}/issues', headers=headers, params={'state': 'all'})
issues_data = issues_response.json()

open_issues = len([issue for issue in issues_data if issue['state'] == 'open'])
closed_issues = len(issues_data) - open_issues

# Prepare the markdown report
report = f"""# Repository Report

## Commits

Total Commits: {len(commits_data)}

### Commit Details
"""
for commit in commits_data:
    report += f"- {commit['commit']['message']} by {commit['commit']['author']['name']}\n"

report += f"""

## Issues

- Open Issues: {open_issues}
- Closed Issues: {closed_issues}
"""

# Save the report to a markdown file
with open('REPORT.md', 'w') as file:
    file.write(report)
