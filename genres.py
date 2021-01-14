import requests
import pandas as pd
from bs4 import BeautifulSoup
genre_list = []
url = pd.read_csv('urls.csv')
url1 = url.head(1000)
url2 = url1.values.tolist()
for i in range(len(url2)):
    genre = requests.get(url2[i][0].strip("[']"))
    genre1 = BeautifulSoup(genre.content, 'html.parser')
    genree = []
    try:
        genre_list.append([genre1.find_all('a', class_='actionLinkLite bookPageGenreLink')[0:3][l].get_text() for l in range(3)])
    except (AttributeError, IndexError):
        for k in range(3):
            genree.append('ERROR HERE!!!!!!!!!!')
    print(genre_list)
    genree.clear()
genres = pd.DataFrame(data=genre0)
genres.columns = ['Genres']
genres.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\genres.csv', index=False)
