import requests
from bs4 import BeautifulSoup

url = 'http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum'
res = requests.get(url).text 
soup = BeautifulSoup(res, 'html.parser')


mons = soup.select('#asiaBody > table > tbody > tr')

for mon in mons:
    print(mon.select_one("td.name").text)
    print(mon.select_one("td.idx").text)
    print("---------------")
#asiaBody > table > tbody > tr.fst.link
