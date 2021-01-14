import requests
import pandas as pd
from bs4 import BeautifulSoup
title0 = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    title = requests.get(url2[i][0].strip("[']"))
    title1 = BeautifulSoup(title.content, 'lxml.parser')
    try:
        title2 = title1.find('h1', class_='gr-h1 gr-h1--serif').get_text().strip('\n').strip(' ')
        title0.append(title2)
        print(title2)
    except AttributeError:
        title0.append('MOVIE NAME MISSING!!!!!!!!!!')
        print('MOVIE NAME MISSING!!!!!!!!!!')
titles = pd.DataFrame(data=title0)
titles.columns = ['Title']
titles.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\titles.csv', index=False)
