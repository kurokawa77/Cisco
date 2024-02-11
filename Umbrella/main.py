# API Keys or Legacy Keys may be needed when you seeing 403 forbidden error message.
#
print("\n")
import requests
import sys
import json
# to solve bug with Umbrella redirect
from requests import Session


class NoRebuildAuthSession(Session):
    def rebuild_auth(self, prepared_request, response):
        """
        No code here means requests will always preserve the Authorization
        header when redirected.
        Be careful not to leak your credentials to untrusted hosts!
        """


session = NoRebuildAuthSession()

# adds /home to the path to import environment module
sys.path.insert(0, '/Users/taka')

# import API key module
import environment as env

# set global variables
umb_token_url = "https://management.api.umbrella.com/auth/v2/oauth2/token"
umb_client_id = env.UMBRELLA_REPORTING_KEY
umb_client_secret = env.UMBRELLA_REPORTING_SECRET
umb_org_id = env.UMBRELLA_ORG_ID

'''
Function to retrieve Umbrella OAuth token
'''


def get_access_token():
    try:
        payload = {}
        response = requests.post(umb_token_url, data=payload, auth=(umb_client_id, umb_client_secret))
        response.raise_for_status()
    except Exception as error:
        print(error)
        return None
    else:
        #print(response.json()['access_token'])
        return response.json()['access_token']


'''
Function to retrieve Umbrella reporting summary
'''


def get_umbrella_summary():
    try:
        # retrieve Umbrella access token
        umb_access_token = get_access_token()
        payload = {}
        #print(umb_access_token)
        # reporting query to retrieve all blocked activity from the past 7 days
        url = f"https://reports.api.umbrella.com/v2/organizations/{umb_org_id}/summary?from=-7days&to=now"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {umb_access_token}"
        }
        # API call to reporting v2 API
        response = session.get(url, headers=headers, data=payload)
        response.raise_for_status()
    # error handling
    except Exception as error:
        print(f"Reporting API call failed for error: {error}")
    else:
        print(json.dumps(response.json(), indent=4))
        return response.json()


if __name__ == '__main__':
    # get security summary from Umbrella
    print("\nThis is Org ID:", umb_org_id)
    get_umbrella_summary = get_umbrella_summary()
    print(get_umbrella_summary)