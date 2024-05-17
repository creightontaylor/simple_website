import datetime

# Function to generate a unique filename based on the current date
def generate_filename():
    today = datetime.date.today()
    filename = f'daily_summary_{today}.md'
    return filename

# Function to save the markdown report to a file
def save_report(report_content):
    filename = generate_filename()
    with open(filename, 'w') as file:
        file.write(report_content)

if __name__ == '__main__':
    # Example usage
    report_content = '# Report\nThis is a generated report.'
    save_report(report_content)