import requests
import pandas as pd
from bs4 import BeautifulSoup
place0 = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    place = requests.get(url2[i][0].strip("[']"))
    place1 = BeautifulSoup(place.content, 'html.parser')
    place0.append(', '.join([place.get_text() for m, place in enumerate(place1.find_all('a')) if str(place).split('/')[1] == 'places']))
    print(place0)
places = pd.DataFrame(data=place0)
places.columns = ['Places']
places.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\places.csv', index=False)