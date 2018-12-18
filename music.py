import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'html.parser')

music_table = soup.select("table tr.lst50")

musics = soup.select('table tbody tr')
for music in music_table:
    number = music.select_one("span.rank").text
    title = music.select_one("div.wrap_song_info a").text
     print(number +"위 : "+ title)