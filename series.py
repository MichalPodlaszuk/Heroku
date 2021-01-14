import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import numpy as np
series0 = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    series = requests.get(url2[i][0].strip("[']"))
    series1 = BeautifulSoup(series.content, 'html.parser')
    try:
        series0.append([1 if series1.find('a', class_='greyText').get_text().strip('\n').strip(' ') != 'Edit Details' else 0])
        print(series0)
    except AttributeError:
        series0.append('ERROR HERE!!!!!!')
        print('ERROR HERE!!!!!!')
serie = pd.DataFrame(data=series0)
serie.columns = ['Series']
time.sleep(10)
for i in range(len(serie)):
    serie.iloc[i] = (serie.iloc[i] != 'Edit Details').values
serie.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\series.csv', index=False)
