import requests
import pandas as pd
from bs4 import BeautifulSoup
review0 = []
url = pd.read_csv('urls.csv')
url1 = url.values.tolist()
for i in range(len(url1)):
    review = requests.get(url1[i][0].strip("[']"))
    review1 = BeautifulSoup(review.content, 'lxml.parser')
    try:
        review2 = ''.join(review1.find('meta', itemprop='reviewCount').get_text().strip('\n').strip(' ').strip('reviews').strip(' ').strip('\n').split(','))
        review0.append(int(review2))
        print(int(review2))
    except AttributeError:
        review0.append('ERROR HERE!!!!!!!!!!')
        print('ERROR HERE!!!!!!!!!!')
reviews = pd.DataFrame(data=review0)
reviews.columns = ['Number of reviews']
reviews.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\reviews.csv', index=False)