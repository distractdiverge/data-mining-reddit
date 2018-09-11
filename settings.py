import os
from dotenv import load_dotenv
load_dotenv()

REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
if REDDIT_CLIENT_ID is None:
    raise EnvironmentError('Missing environment variable "REDDIT_CLIENT_ID"')

REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
if REDDIT_CLIENT_SECRET is None:
    raise EnvironmentError('Missing environment variable "REDDIT_CLIENT_SECRET"')

REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')
if REDDIT_USER_AGENT is None:
    raise EnvironmentError('Missing environment variable "REDDIT_USER_AGENT"')