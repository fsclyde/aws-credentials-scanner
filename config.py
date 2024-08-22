# Regular expression patterns for AWS Access Key ID and Secret Access Key
AWS_ACCESS_KEY_PATTERN = r'AKIA[0-9A-Z]{16}'
AWS_SECRET_KEY_PATTERN = r'(?P<key>[A-Za-z0-9/+=]{40})'

# Logging Configuration
LOGGING_MESSAGE_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
