import datetime
import json
from fetch_data import fetch_commits, fetch_issues

# Fetch data
commits_data = fetch_commits()
issues_data = fetch_issues()

# Extract data
number_of_commits = len(commits_data)
commit_messages = [f'{commit['author']}: {commit['message']}' for commit in commits_data]
open_issues = len([issue for issue in issues_data if issue['state'] == 'open'])
closed_issues = len([issue for issue in issues_data if issue['state'] == 'closed'])

def generate_markdown_report():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    report_content = f'# Daily Summary Report - {date}\n\n'
    report_content += f'## Number of Commits\n{number_of_commits}\n\n'
    report_content += '## Commit Messages with Author Names\n'
    for message in commit_messages:
        report_content += f'- {message}\n'
    report_content += '\n'
    report_content += f'## Open Issues: {open_issues}\n'
    report_content += f'## Closed Issues: {closed_issues}\n'

    with open('../daily_summary.md', 'w') as file:
        file.write(report_content)

if __name__ == '__main__':
    generate_markdown_report()
