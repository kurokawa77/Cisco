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

admin_api = duo_client.Admin(
    ikey=duo_integration_key,
    skey=duo_secret_key,
    host=duo_api_host
)

users = admin_api.get_users()

#Disable or Activate the user
#user_id = ""
#for user in users:
#    if user['username'] == "granite":
#        user_id = user['user_id']
#        print(f"\nThis is the user ID of {user['username']}: {user_id}")

# disable a user
#admin_api.update_user(user_id=user_id, status="disabled")
#admin_api.update_user(user_id=user_id, status="active")

#users = admin_api.get_users()

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