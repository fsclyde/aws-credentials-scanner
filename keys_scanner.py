"""
   Function that scan the keys
"""

import boto3
import re
from botocore.exceptions import NoCredentialsError, ClientError
import config

# Keys Check
class KeysCheck:
    def __init__(self, logger):
        self.logger = logger

    def scan_for_aws_keys(self, lines):

        credentials = []
        access_key_count = 0

        for i, line in enumerate(lines):
            if re.search(config.AWS_ACCESS_KEY_PATTERN, line):
                access_key = re.search(config.AWS_ACCESS_KEY_PATTERN, line).group()
                access_key_count += 1
                # Check the secret keu in the second line
                if i + 1 < len(lines):
                    secret_key_match = re.search(config.AWS_SECRET_KEY_PATTERN, lines[i + 1])
                    if secret_key_match:
                        secret_key = secret_key_match.group('key')
                        credentials.append({
                            'access_key': access_key,
                            'secret_key': secret_key,
                            'line_number': i + 1
                        })
        return credentials, access_key_count

    def validate_aws_credentials(self, access_key, secret_key):
        """ Validate AWS credentials with STS """
        try:
            session = boto3.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key
            )
            sts = session.client('sts')
            identity = sts.get_caller_identity()
            return True, identity
        except (NoCredentialsError, ClientError):
            return False, None

    def extract_code_block(self, lines, line_number):
        """ Extract a block of code around the detected key """
        start = max(line_number - 3, 0)
        end = min(line_number + 3, len(lines))
        return ''.join(lines[start:end])

