import requests
from datetime import datetime

# GitHub API base URL
BASE_URL = 'https://api.github.com'

# Function to fetch daily commits
def fetch_daily_commits(owner, repo):
    today = datetime.now().strftime('%Y-%m-%d')
    commits_url = f'{BASE_URL}/repos/{owner}/{repo}/commits?since={today}T00:00:00Z'
    response = requests.get(commits_url)
    commits_data = response.json()

    daily_commits = []
    for commit in commits_data:
        commit_info = {
            'message': commit['commit']['message'],
            'author': commit['commit']['author']['name']
        }
        daily_commits.append(commit_info)

    return daily_commits

# Function to fetch issues count by state
def fetch_issues_count(owner, repo):
    issues_url = f'{BASE_URL}/repos/{owner}/{repo}/issues'
    response = requests.get(issues_url)
    issues_data = response.json()

    open_issues = len([issue for issue in issues_data if issue['state'] == 'open'])
    closed_issues = len([issue for issue in issues_data if issue['state'] == 'closed'])

    return {'open_issues': open_issues, 'closed_issues': closed_issues}

# Example usage
if __name__ == '__main__':
    owner = 'exampleOwner'
    repo = 'exampleRepo'

    daily_commits = fetch_daily_commits(owner, repo)
    issues_count = fetch_issues_count(owner, repo)

    print('Daily Commits:', daily_commits)
    print('Issues Count:', issues_count)
