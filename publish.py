import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
publish0 = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    publish = requests.get(url2[i][0].strip("[']"))
    publish1 = BeautifulSoup(publish.content, 'html.parser')
    publish2 = publish1.find_all('div', class_='row')
    try:
        publish3 = publish2[1].get_text().strip('\n').split(' ')
        publish0.append([item for n, item in enumerate(publish3.strip('\n')) if item.isnumeric()])
        print(publish0)
    except (AttributeError, IndexError):
        publish0.append('ERROR HERE!!!!!!!!!!')
        print('ERROR HERE!!!!!!!!!!')
publishes = pd.DataFrame(data=publish0)
publishes.columns = ['Publish year']
publishes.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\publishes.csv', index=False)