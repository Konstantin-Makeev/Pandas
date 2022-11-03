import requests
from bs4 import BeautifulSoup

data = []
url = 'https://en.wikipedia.org/wiki/Life_expectancy'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find(class_='wikitable')
tbody = table.find('tbody')
trs = tbody.find_all('tr')
for tr in trs:
    tds = tr.select('td')
    if tds:
        print(tds[0].string)
    print(tr)