import re
from process_data import get_processed_data


def validate_markdown(md_content):
    """Validate markdown format.

    Args:
        md_content (str): The markdown content to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Simple markdown validation (can be expanded as needed)
    is_valid = bool(re.match(r'^#.*\n(\n.*\n)*', md_content))
    return is_valid


def generate_markdown_report():
    """Generate markdown report from processed data."""
    data = get_processed_data()
    date = data['date']
    commit_details = data['commit_details']
    issue_counts = data['issue_counts']

    markdown_content = f"""
# Report Date: {date}

## Commit Details
{commit_details}

## Issue Counts
{issue_counts}
    """

    if validate_markdown(markdown_content):
        return markdown_content
    else:
        raise ValueError('Invalid Markdown Format')


if __name__ == '__main__':
    report = generate_markdown_report()
    print(report)
