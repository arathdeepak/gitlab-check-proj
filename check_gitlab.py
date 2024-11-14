import gitlab
from datetime import datetime, timedelta
import pytz

# Function to authenticate with GitLab (disable SSL verification)
def authenticate_gitlab(private_token):
    gl = gitlab.Gitlab('https://gitlab.com', private_token=private_token, ssl_verify=False)
    return gl

# Function to check if a project is unused based on the last commit date
def is_project_unused(project, days_threshold):
    commits = project.commits.list(per_page=1)  # Get the most recent commit
    if not commits:
        return True  # If there are no commits, consider it unused
    
    last_commit_date = commits[0].created_at
    commit_datetime = datetime.strptime(last_commit_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    commit_datetime = pytz.UTC.localize(commit_datetime)
    
    threshold_datetime = datetime.now(pytz.UTC) - timedelta(days=days_threshold)
    
    return commit_datetime < threshold_datetime

# Function to get unused projects in a group
def find_unused_projects(group, days_threshold):
    unused_projects = []
    projects = group.projects.list(all=True)
    
    for project in projects:
        if is_project_unused(project, days_threshold):
            unused_projects.append(project)
    
    return unused_projects

def main():
    private_token = 'your_gitlab_private_token'  # Replace with your GitLab private token
    group_name = 'your_group_name'  # Replace with your GitLab group name
    days_threshold = 180  # Define the threshold (e.g., 180 days without activity)
    
    gl = authenticate_gitlab(private_token)
    group = gl.groups.get(group_name)
    
    unused_projects = find_unused_projects(group, days_threshold)
    
    if unused_projects:
        print(f"Found {len(unused_projects)} unused projects:")
        for project in unused_projects:
            print(f"- {project.name} (Last commit: {project.last_activity_at})")
    else:
        print("No unused projects found.")

if __name__ == "__main__":
    main()
