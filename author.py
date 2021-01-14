import requests
import pandas as pd
from bs4 import BeautifulSoup
author_list = []
url = pd.read_csv('urls.csv').head(1000).values.tolist()
for index, link in enumerate(url):
    author = BeautifulSoup(requests.get(link[0].strip("[']")).content, 'html.parser')
    try:
        author_list.append(author.find('span', itemprop='name').get_text())
    except AttributeError:
        author_list.append('')
authors = pd.DataFrame(data=author_list)
authors.columns = ['Author']