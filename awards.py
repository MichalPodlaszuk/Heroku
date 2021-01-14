import requests
import pandas as pd
from bs4 import BeautifulSoup
award0 = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    award = requests.get(url2[i][0].strip("[']"))
    award1 = BeautifulSoup(award.content, 'html.parser')
    awardd = []
    try:
        award0.append([award1.find_all('a', class_='award')[j].get_text() for j, award in enumerate(award1.find_all('a', class_='award'))])
        print(award0)
    except (AttributeError, IndexError):
        award2 = award1.find_all('a', class_='award')
        for k in range(len(award2)):
            awardd.append('ERROR HERE!!!!!!!!')
        award0.append(', '.join(awardd))
    awardd.clear()
awards = pd.DataFrame(data=award0)
awards.columns = ['Awards']
awards.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\awards.csv', index=False)