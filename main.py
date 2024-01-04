import requests
from bs4 import BeautifulSoup




def get_html(date:str):
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    html = requests.get(url)
    return html

#make sure you acess just the names of the song and no HTML info

# create an input statement 
date = str(input("What year do you want to be taken back to? (use YYYY-MM-DD format):"))

soup = BeautifulSoup(get_html(date).text, 'html.parser')
soup.get_text()


elements = soup.select('li #title-of-a-story')

for i in range(len(elements)):
    elements[i] = elements[i].get_text()


for i in range(len(elements)):
    elements[i] = elements[i].replace('\n', '')
    elements[i] = elements[i].replace('\t', '')
    



