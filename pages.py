import requests
import pandas as pd
from bs4 import BeautifulSoup
page0 = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    page = requests.get(url2[i][0].strip("[']"))
    page1 = BeautifulSoup(page.content, 'html.parser')
    try:
        page2 = page1.find('span', itemprop='numberOfPages').get_text().strip(' pages')
        page0.append(page2)
        print(page2)
    except AttributeError:
        page0.append('MOVIE NAME MISSING!!!!!!!!!!')
        print('MOVIE NAME MISSING!!!!!!!!!!')
pages = pd.DataFrame(data=page0)
pages.columns = ['Pages']
pages.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\pages.csv', index=False)
