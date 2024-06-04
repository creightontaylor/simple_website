import datetime
import json

# Assuming data fetching and processing is already implemented

def generate_markdown_summary(data):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    commits = data.get('commits', [])
    open_issues = data.get('open_issues', 0)
    closed_issues = data.get('closed_issues', 0)

    with open('daily_summary.md', 'w') as md_file:
        md_file.write(f'# Daily Summary for {date_str}\n\n')
        md_file.write(f'## Commits ({len(commits)}):\n')
        for commit in commits:
            md_file.write(f'- {commit}\n')
        md_file.write(f'\n## Open Issues: {open_issues}\n')
        md_file.write(f'## Closed Issues: {closed_issues}\n')

# Example usage
# Assuming `data` is fetched and processed elsewhere in the script
# data = {
#     'commits': ['Fix bug in X', 'Improve performance of Y'],
#     'open_issues': 10,
#     'closed_issues': 5,
# }
# generate_markdown_summary(data)