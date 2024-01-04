# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
# # write your client ID and secret 
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
scope = "playlist-modify-private"
# #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")



# Shows the top artists for a user


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

def find_song(songs):
    result = sp.search(son)



pprint.pprint(result['tracks']['items'][0]['uri'])