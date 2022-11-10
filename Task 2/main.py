import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

data = {'Era': [], 'Life expectancy at birth in years': [], 'Notes': []}
url = 'https://en.wikipedia.org/wiki/Life_expectancy'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find(class_='wikitable')
tbody = table.find('tbody')
trs = tbody.find_all('tr')
for tr in trs:
    tds = tr.select('td')
    if tds:
        data['Era'].append(re.sub(r'\[\d+\]|\n', '', tds[0].text))
        data['Life expectancy at birth in years'].append(re.sub(r'\[\d+\]|\n', '', tds[1].text))
        data['Notes'].append(re.sub(r'\[\d+\]|\n', '', tds[2].text))
df = pd.DataFrame(data)
print(df)