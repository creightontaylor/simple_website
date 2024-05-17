# Import necessary modules from fetch_data.py
from fetch_data import get_commit_data, get_issue_data

# Function to parse commit data
def parse_commit_data(commit_data):
    parsed_data = []
    for commit in commit_data:
        commit_info = {
            'author': commit['commit']['author']['name'],
            'message': commit['commit']['message']
        }
        parsed_data.append(commit_info)
    return parsed_data

# Function to count open and closed issues
def count_issues(issue_data):
    open_issues = sum(1 for issue in issue_data if issue['state'] == 'open')
    closed_issues = sum(1 for issue in issue_data if issue['state'] == 'closed')
    return {'open_issues': open_issues, 'closed_issues': closed_issues}

# Main function to process data
if __name__ == '__main__':
    commit_data = get_commit_data()
    issue_data = get_issue_data()
    
    parsed_commits = parse_commit_data(commit_data)
    issue_counts = count_issues(issue_data)
    
    # Structured data ready to be formatted into markdown
    structured_data = {
        'commits': parsed_commits,
        'issues': issue_counts
    }
    
    print(structured_data)