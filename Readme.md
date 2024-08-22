# Credentials Scanner Tool

## Overview

This script is designed to detect hardcoded AWS credentials within a local Git repository. It checks for both AWS Access Key IDs and AWS Secret Access Keys in your codebase and validates them. If valid credentials are found, it logs their presence, providing details on the file and caller identity.
Requirements

## Project Structure

bash

    credentials-scanner/
    │
    ├── README.md           # Project documentation
    ├── utils.py            # Shared modules for the scripts
    ├── keys_scanner.py     # Functions that scan for AWS access keys
    ├── main.py             # Main function of the module
    ├── config.py           # Configurations of the module
    └── requirements.txt    # Python dependencies

### Before running the script, ensure you have the following:

    Python 3.x
    Required gitpython

### Usage

To run the script, use the command line with the following syntax:

    pip3 install -r requirements.txt
    python main.py <path_to_local_git_repo>

#### Parameters

    <path_to_local_git_repo>: The absolute or relative path to the local Git repository you want to scan.

#### Example

    python main.py /path/to/my/git/repo

### How It Works

    Initial Checks:
        The script verifies that exactly one argument is provided.
        It checks if the given path is a valid directory and if it contains a .git folder, confirming it's a Git repository.

    Scanning for AWS Keys:
        The script scans the repository for hardcoded AWS Access Keys using a predefined pattern (AWS_ACCESS_KEY_PATTERN).
        It then scans for AWS Secret Keys using another predefined pattern (AWS_SECRET_KEY_PATTERN).

    Validation:
        If potential AWS Access Keys and Secret Keys are found, the script attempts to validate them using AWS APIs.
        It logs whether the detected credentials are valid or invalid, along with the file name and caller identity for valid credentials.


#### Example Output

If no credentials are found, you will see:

    TIMESTAMP - INFO - Branch: 
    TIMESTAMP - INFO - Commit ID: 
    TIMESTAMP - INFO - Author: 
    TIMESTAMP - INFO - Message: 
    TIMESTAMP - INFO - Timestamp: 
    TIMESTAMP - INFO - File Name: 
    TIMESTAMP - INFO - Line Number: 
    TIMESTAMP - INFO - Credentials Valid: 
    TIMESTAMP - INFO - Code Block:


### Customization

    Patterns: Adjust config.AWS_ACCESS_KEY_PATTERN and config.AWS_SECRET_KEY_PATTERN to match your specific key formats.
    Logger Configuration: Modify the Logger class for custom logging behaviors.