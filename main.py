"""
   Main function
"""
from git import Repo
from utils import Logger, check_if_file_exists, check_if_directory, logging
import sys
import os
from keys_scanner import KeysCheck

# main function of the script
def main():
    # Initialize logger
    Mylogger = Logger()
    MyKeysCheck = KeysCheck(Mylogger)

    if len(sys.argv) != 2:
        Mylogger.log("Usage: python main.py <path_to_local_git_repo>", level=logging.ERROR)
        sys.exit(1)

    repo_path = sys.argv[1]

    if not os.path.isdir(repo_path):
        Mylogger.log(f"Error: {repo_path} is not a valid directory.", level=logging.ERROR)
        sys.exit(1)

    if not os.path.isdir(os.path.join(repo_path, '.git')):
        Mylogger.log(f"Error: {repo_path} is not a valid Git repository.", level=logging.ERROR)
        sys.exit(1)

    # Initialize Git repository
    repo = Repo(repo_path)

    # Get a list of all branches in the repository
    branches = repo.branches

    for branch in branches:
        Mylogger.log(f"Scanning branch: {branch}")
        repo.git.checkout(branch)

        for commit in repo.iter_commits(branch):

            commit_id = commit.hexsha
            author = commit.author.name
            message = commit.message.strip()
            timestamp = commit.committed_datetime.isoformat()

            for entry in commit.tree.traverse():
                file_path = os.path.join(repo_path, entry.path)

                if not check_if_directory(file_path) and check_if_file_exists(file_path):
                    with open(file_path, 'r') as file:
                        lines = file.readlines()
                    credentials, access_key_count = MyKeysCheck.scan_for_aws_keys(lines)

                    if credentials:
                        for cred in credentials:
                            block = MyKeysCheck.extract_code_block(lines, cred['line_number'])
                            is_valid, identity_or_error = MyKeysCheck.validate_aws_credentials(cred['access_key'],
                                                                                               cred['secret_key'])
                            Mylogger.log(f"Branch: {branch}")
                            Mylogger.log(f"Commit ID: {commit_id}")
                            Mylogger.log(f"Author: {author}")
                            Mylogger.log(f"Message: {message}")
                            Mylogger.log(f"Timestamp: {timestamp}")
                            Mylogger.log(f"File Name: {file_path}")
                            Mylogger.log(f"Line Number: {cred['line_number']}")
                            Mylogger.log(f"Credentials Valid: {'Yes' if is_valid else 'No'}")
                            Mylogger.log(f"Number of Access Key Detections: {access_key_count}")
                            Mylogger.log("Code Block:")
                            Mylogger.log(block)

if __name__ == "__main__":
    main()
