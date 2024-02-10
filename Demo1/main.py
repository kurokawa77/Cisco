# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pprint
import sys
import duo_client

# adds /home to the path to import environment module
sys.path.insert(0, '/Users/taka')

# import API key module
import environment as env
duo_integration_key = env.DUO_INTEGRATION_KEY
duo_secret_key = env.DUO_SECRET_KEY
duo_api_host = env.DUO_API_HOST

print(duo_integration_key)
