import os
import requests
import shelve
import time
# Securely access GitHub Personal Access Token from environment variables
# To set up this environment variable, use the following command in your terminal or CI/CD pipeline:
# export GITHUB_TOKEN='your_personal_access_token_here'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_REPO = 'https://api.github.com/repos/username/repository'

# Headers to authenticate with GitHub API using the token
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Fetch the number of commits
cache_key = 'commits_data'
with shelve.open('api_cache') as cache:
    if cache_key in cache and time.time() - cache[cache_key]['timestamp'] < 86400:
        commits_data = cache[cache_key]['data']
    else:
        for attempt in range(5):
            try:
                commits_response = requests.get(f'{GITHUB_REPO}/commits', headers=headers)
                commits_response.raise_for_status()
                break
            except requests.exceptions.HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                time.sleep(2 ** attempt)
            except Exception as err:
                print(f'Other error occurred: {err}')
                time.sleep(2 ** attempt)
            else:
                commits_data = commits_response.json()
                cache[cache_key] = {'data': commits_data, 'timestamp': time.time()}
        commits_data = commits_response.json()
        cache[cache_key] = {'data': commits_data, 'timestamp': time.time()}

# Fetch the number of open and closed issues
cache_key = 'issues_data'
with shelve.open('api_cache') as cache:
    if cache_key in cache and time.time() - cache[cache_key]['timestamp'] < 86400:
        issues_data = cache[cache_key]['data']
    else:
        for attempt in range(5):
            try:
                issues_response = requests.get(f'{GITHUB_REPO}/issues', headers=headers, params={'state': 'all'})
                issues_response.raise_for_status()
                break
            except requests.exceptions.HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                time.sleep(2 ** attempt)
            except Exception as err:
                print(f'Other error occurred: {err}')
                time.sleep(2 ** attempt)
            else:
                issues_data = issues_response.json()
                cache[cache_key] = {'data': issues_data, 'timestamp': time.time()}
        issues_data = issues_response.json()
        cache[cache_key] = {'data': issues_data, 'timestamp': time.time()}

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
with open('daily_summary.md', 'w') as file:
    file.write(report)
