"""
    This module have all shared functions for the solution
"""
import os
import logging
import config

# Check if directory
def check_if_directory(path):
    if os.path.isdir(path):
        return True
    else:
        return False

# Check if file exist
def check_if_file_exists(path):
    if os.path.isfile(path):
        return True
    else:
        return False

# Logger setup
class Logger:
    def __init__(self):
        self.logger = logging.getLogger('CredentialsDetector')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(config.LOGGING_MESSAGE_FORMAT)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)
