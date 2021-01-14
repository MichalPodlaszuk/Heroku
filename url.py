import requests
import pandas as pd
from bs4 import BeautifulSoup
url0 = []
k = 1
while k < 36:
    url = requests.get(f'https://www.goodreads.com/list/show/47.Best_Dystopian_and_Post_Apocalyptic_Fiction?page={k}')
    url1 = BeautifulSoup(url.content, 'html.parser')
    url2 = url1.find_all('a')
    url3 = url2[132:1124]
    url4 = url3[0:991:10]
    for i in range(len(url4)):
        url5 = str(url4[i]).split('>')
        url6 = str(url5[0]).split(' ')
        url7 = str(url6[1]).split('"')
        href = url7[1]
        url0.append('https://www.goodreads.com/'+href)
    k+=1
while k == 36:
    url = requests.get(f'https://www.goodreads.com/list/show/47.Best_Dystopian_and_Post_Apocalyptic_Fiction?page={k}')
    url1 = BeautifulSoup(url.content, 'html.parser')
    url2 = url1.find_all('a')
    url3 = url2[132:174]
    url4 = url3[0:41:10]
    for i in range(len(url4)):
        url5 = str(url4[i]).split('>')
        url6 = str(url5[0]).split(' ')
        url7 = str(url6[1]).split('"')
        href = url7[1]
        url0.append('https://www.goodreads.com/' + href)
    k+=1
urls = pd.DataFrame(data=url0)
urls.columns = ['URL']
urls.to_csv(r'C:\Users\ziolo\PycharmProjects\BuildWeek\urls.csv', index=False)
