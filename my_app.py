
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

def find_song(song:str):
    result = sp.search(song)
    list_of_songs = result['tracks']['items']
    for i in range(len(list_of_songs)):
        if list_of_songs[i]['name'] == song:
            song_uri= list_of_songs[i]['uri']
            return song_uri
    


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private"))

user_info = sp.current_user()
spotify_username = user_info["id"]





