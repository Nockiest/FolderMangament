import os
import subprocess
import requests
from getpass import getpass

def initialize_git_repo(folder_path):
    # Check if a Git repository already exists
    if not os.path.exists(os.path.join(folder_path, '.git')):
        # If not, initialize a new Git repository
        subprocess.run(['git', 'init'], cwd=folder_path)
        print('Initialized a new Git repository.')

def create_github_repo(repo_name, github_token):
    # GitHub API endpoint for creating a new repository
    url = 'https://api.github.com/user/repos'

    # Repository data
    data = {
        'name': repo_name,
        'private': False,  # Set to True if you want a private repository
    }

    # Headers including the GitHub token for authentication
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    # Make a POST request to create the repository
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f'GitHub repository "{repo_name}" created successfully.')
    else:
        print(f'Failed to create GitHub repository. Status code: {response.status_code}')
        print(response.text)
        exit()

def add_and_commit_files(folder_path):
    # Add all files to the Git staging area
    subprocess.run(['git', 'add', '.'], cwd=folder_path)

    # Commit the changes
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=folder_path)
    print('Committed initial changes.')

def main():
    # Specify the folder path
    folder_path = os.getcwd()
    question = input('Do you really want to proceed? [y]')
    if question.lower() != 'y':
        print('Aborted.')
        return
    # GitHub repository name
    repo_name =  repo_name = os.path.basename(os.path.normpath(folder_path)) + '-repo'

    # GitHub token for authentication
    github_token = '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' #getpass('Enter your GitHub token: ')

    # Initialize the Git repository if it doesn't exist
    initialize_git_repo(folder_path)

    # Create a GitHub repository
    create_github_repo(repo_name, github_token)

    # Add and commit files to the GitHub repository
    add_and_commit_files(folder_path)

if __name__ == '__main__':
    main()