import requests
import pandas as pd
from bs4 import BeautifulSoup
rating0 = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    rating = requests.get(url2[i][0].strip("[']"))
    rating1 = BeautifulSoup(rating.content, 'html.parser')
    try:
        rating2 = rating1.find('span', itemprop='ratingValue').get_text()
        rating0.append(float(rating2.strip('\n').strip(' ')))
        print(float(rating2.strip('\n').strip(' ')))
    except AttributeError:
        rating0.append('ERROR HERE!!!!!!!!!!')
        print('ERROR HERE!!!!!!!!!!')
ratings = pd.DataFrame(data=rating0)
ratings.columns = ['Average rating']
ratings.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\avg_ratings.csv', index=False)