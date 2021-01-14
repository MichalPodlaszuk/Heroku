import requests
import pandas as pd
from bs4 import BeautifulSoup
rating0 = []
url = pd.read_csv('urls.csv')
url1 = url.values.tolist()
for i in range(len(url1)):
    rating = requests.get(url1[i][0].strip("[']"))
    rating1 = BeautifulSoup(rating.content, 'html.parser')
    try:
        rating2 = ''.join(rating1.find('meta', itemprop='ratingCount').get_text().strip('\n').strip(' ').strip('ratings').strip(' ').strip('\n').split(','))
        rating0.append(int(rating2))
        print(int(rating2))
    except AttributeError:
        rating0.append('ERROR HERE!!!!!!!!!')
        print('ERROR HERE!!!!!!!!!')
ratings = pd.DataFrame(data=rating0)
ratings.columns = ['Number of ratings']
ratings.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\ratings.csv', index=False)