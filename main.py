import requests
from bs4 import BeautifulSoup
import my_app



def get_html(date:str):
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    html = requests.get(url)
    return html

#make sure you acess just the names of the song and no HTML info

# create an input statement 
date = str(input("What year do you want to be taken back to? (use YYYY-MM-DD format):"))
significance = str(input('what is the significance of this date? (In 3 words)'))

soup = BeautifulSoup(get_html(date).text, 'html.parser')
soup.get_text()


songs = soup.select('li #title-of-a-story')

for i in range(len(songs)):
    songs[i] = songs[i].get_text()


for i in range(len(songs)):
    songs[i] = songs[i].replace('\n', '')
    songs[i] = songs[i].replace('\t', '')
    

uri_list = []
for song in songs:
    if my_app.find_song(song) != None:
        uri_list.append(my_app.find_song(song))


playlist_name = significance
playlist_description = "Time for you to be taken back to:" + date
playlist_id = my_app.sp.user_playlist_create(user=my_app.spotify_username, name=playlist_name, public=False, description=playlist_description)["id"]



my_app.sp.user_playlist_add_tracks(user=my_app.spotify_username, playlist_id=playlist_id, tracks=uri_list)
    


