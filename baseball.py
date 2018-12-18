import requests
from bs4 import BeautifulSoup 

url = 'https://www.melon.com/chart/index.htm'
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')

balls = soup.select('table')
for ball in balls:
    print(ball.select_one("td:nts-of-type(1) a strong").text)
