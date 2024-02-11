# This is a sample Python script.
# Reference https://developer.cisco.com/learning/labs/sase-2-duo/creating-and-reading-users-with-duo-admin-api/
# you need to add environment.py for editting various key

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

duo_api = duo_client.Admin(
    ikey=duo_integration_key,
    skey=duo_secret_key,
    host=duo_api_host
)

# Retrieve users
#users = duo_api.get_users()

# Retrieve users with try and except function
try:
    users = duo_api.get_users()
except duo_client.DuoAPIError as e:
    print(f"Failed to retrieve users: {e}")
    exit(1)

# Create and return a new user object.
'''
user = duo_api.add_user(
    username="granite2",
    realname="granite2",
)
'''
# Delete user
'''
user_id = ""
for user in users:
    if user['username'] == "testaccount":
        user_id = user['user_id']
        print(f"\nThis is the user ID of {user['username']}: {user_id}")

user = duo_api.delete_user(user_id=user_id)
print(user)
'''

#Disable or Activate the user
#user_id = ""
#for user in users:
#    if user['username'] == "granite":
#        user_id = user['user_id']
#        print(f"\nThis is the user ID of {user['username']}: {user_id}")

# disable a user
#duo_api.update_user(user_id=user_id, status="disabled")
#duo_api.update_user(user_id=user_id, status="active")

#users = admin_api.get_users()
users = duo_api.get_users()

print("Username\t\tStatus")
print("------------------")
for user in users:
    print(f"{user['username']}\t{user['status']}")
#
#
#
#
#
#