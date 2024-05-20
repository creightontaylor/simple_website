import requests
import datetime
import os

# GitHub API URL
API_URL = 'https://api.github.com/repos/USERNAME/REPOSITORY'

# Get today's date
today = datetime.date.today().isoformat()

# Path for the daily summary report
report_path = '../daily_summary.md'

# Check if today's report already exists
def report_exists():
    return os.path.exists(report_path) and today in open(report_path).read()

# Fetch data from GitHub API
def fetch_data():
    # Headers to authenticate and get data in a good format
    headers = {'Authorization': 'token YOUR_GITHUB_TOKEN'}
    # Fetch commits
    commits_response = requests.get(f'{API_URL}/commits?since={today}T00:00:00Z', headers=headers).json()
    # Fetch issues
    issues_response = requests.get(f'{API_URL}/issues?since={today}T00:00:00Z', headers=headers).json()

    # Count open and closed issues
    open_issues = len([issue for issue in issues_response if issue['state'] == 'open'])
    closed_issues = len([issue for issue in issues_response if issue['state'] == 'closed'])

    return len(commits_response), open_issues, closed_issues

# Generate and save the report
def generate_report(commits, open_issues, closed_issues):
    with open(report_path, 'w') as file:
        file.write(f'# Daily Summary for {today}\n')
        file.write(f'## Number of commits: {commits}\n')
        file.write(f'## Open issues: {open_issues}\n')
        file.write(f'## Closed issues: {closed_issues}\n')

if not report_exists():
    commits, open_issues, closed_issues = fetch_data()
    generate_report(commits, open_issues, closed_issues)
    print('Daily summary report generated.')
else:
    print('Today\'s report already exists.')
