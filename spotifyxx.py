import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
username = sys.argv[1]
client_id = '7ff89745005f40478c50114bee30c80f' #placeholder value here
client_secret = 'f57219b980824551a07d8b1e7dc3f6b1' #placeholder value here
redirect_uri = 'http://localhost:8888/callback/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# Erase cache and prompt for user permission
try:
    # token = util.prompt_for_user_token(username, scope) # add scope
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# print(json.dumps(user , sort_keys=True , indent= 4))

displayname = user["display_name"]
followers = user["followers"]["total"]

print("Hi",displayname.split()[0] )
print("Welcome to Ravioli")

# search(q, limit=10, offset=0, type='track', market=None)
# searches for an item
# Parameters:
# q - the search query
# limit - the number of items to return
# offset - the index of the first item to return
# type - the type of item to return. One of ‘artist’, ‘album’,
# ‘track’ or ‘playlist'

while True:

    print("Please choose and Option")
    option = input()

    if option == "0":
        print("Enter an artist you want to search")
        itemToBeScreached = input()
        searchitem = spotifyObject.search(itemToBeScreached , 1, 0 ,"artist")
        print(json.dumps(searchitem , sort_keys=True , indent= 4))
    elif option == "1":
        break