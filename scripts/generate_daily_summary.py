import requests
import os
from urllib.parse import quote_plus

# GitHub API URL
API_URL = 'https://api.github.com'

# GitHub Personal Access Token from Secrets
TOKEN = os.getenv('GITHUB_TOKEN')

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Function to fetch commits
def fetch_commits(repo, date):
    commits_url = f'{API_URL}/repos/{quote_plus(repo)}/commits?since={date}T00:00:00Z&until={date}T23:59:59Z'
    response = requests.get(commits_url, headers=headers)
    if response.status_code == 403:
        raise Exception('API rate limit exceeded')
    elif response.status_code != 200:
        raise Exception('Failed to fetch commits')
    return response.json()

# Function to fetch issue counts
def fetch_issue_counts(repo):
    issues_url = f'{API_URL}/repos/{quote_plus(repo)}/issues?state=all'
    response = requests.get(issues_url, headers=headers)
    if response.status_code == 403:
        raise Exception('API rate limit exceeded')
    elif response.status_code != 200:
        raise Exception('Failed to fetch issues')
    issues = response.json()
    open_issues = len([issue for issue in issues if issue['state'] == 'open'])
    closed_issues = len(issues) - open_issues
    return open_issues, closed_issues

# Main function
if __name__ == '__main__':
    try:
        # Example repository and date
        repository = 'octocat/Hello-World'
        today = '2023-01-01' # This should be dynamically set to the current date

        commits = fetch_commits(repository, today)
        open_issues, closed_issues = fetch_issue_counts(repository)

        print(f'Date: {today}')
        print(f'Commits:')
        for commit in commits:
            print(f'- {commit['commit']['message']} by {commit['commit']['author']['name']}')
        print(f'Open issues: {open_issues}')
         # Save summary to daily_summary.md
         with open('daily_summary.md', 'w') as file:
             file.write(f'Date: {today}\n')
             file.write('Commits:\n')
             for commit in commits:
                 file.write(f'- {commit['commit']['message']} by {commit['commit']['author']['name']}\n')
             file.write(f'Open issues: {open_issues}\n')
             file.write(f'Closed issues: {closed_issues}')
    except Exception as e:
        print(f'Error: {e}')
         # Git add, commit, and push
         os.system('git add daily_summary.md')
         commit_status = os.system('git commit -m "Update daily summary for ' + today + '"')
         if commit_status != 0:
             raise Exception('Git commit failed')
         push_status = os.system('git push')
         if push_status != 0:
             raise Exception('Git push failed')