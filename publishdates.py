#this cell is mine
import requests
import pandas as pd
from bs4 import BeautifulSoup
def scraper():
    urls = []
    author_list= []
    avg_rating_list = []
    award_list = []
    genre_list = []
    number_of_ratings_list = []
    number_of_reviews_list = []
    page_list = []
    places_list = []
    publish_year_list = []
    series_list = []
    titles_list = []
    k=1
    while len(urls) < 1001:
        url_code = requests.get(f'https://www.goodreads.com/list/show/47.Best_Dystopian_and_Post_Apocalyptic_Fiction?page={k}')
        url_raw = BeautifulSoup(url_code.content, 'html.parser').find_all('a')[132:1124:10]
        for i, code in enumerate(url_raw):
            urls.append('https://www.goodreads.com/'+str(code).split('>')[0].split(' ')[1].split('"')[1])
        k+=1
    del urls[1000:-1]
    for j, link in enumerate(urls):
        data_code = requests.get(link[0].strip("[']"))
        data = BeautifulSoup(data_code.content, 'html.parser')
        try:
            author = data.find('span', itemprop='name').get_text()
            author_list.append(author)
            avg_rating = float(data.find('span', itemprop='ratingValue').get_text().strip('\n').split(' '))
            avg_rating_list.append(avg_rating)
            awards = [award.get_text() for k, award in enumerate(data.find_all('a', class_='award'))]
            award_list.append(awards)
            genres = data.find_all('a', class_='actionLinkLite bookPageGenreLink')
            genre_list.append([genres[0:3][l].get_text() for l in range(3)])
            number_of_ratings = int(''.join(data.find('meta', itemprop='ratingCount').get_text().strip('\n ')))
            number_of_ratings_list.append(number_of_ratings.strip('\n ratings').split(','))
            number_of_reviews = int(''.join(data.find('meta', itemprop='reviewCount').get_text().strip('\n ')))
            number_of_reviews_list.append(number_of_reviews.strip('\n reviews').split(','))
            page = data.find('span', itemprop='numberOfPages')
            page_list.append(page.get_text().strip(' pages'))
            places = [data.find_all('a').split('/')[1] == 'places']
            places_list.append(', '.join([place.get_text() for m, place in enumerate(places)]))
            publish_year = data.find_all('div', class_='row')[1].get_text().strip('\n').split(' ')
            publish_year_list.append(item.strip('\n') for n, item in enumerate(publish_year) if item.strip('\n').isnumeric())
            title = data.find('h1', class_='gr-h1 gr-h1--serif')
            titles_list.append(title.get_text().strip('\n').strip(' '))
            series = data.find('a', class_='greyText')
            series_list.append(1 if series.get_text().strip('\n').strip(' ') == 'Edit Details' else 0)
        except (AttributeError, IndexError):
            author_list.append('')
            avg_rating_list.append('')
            award_list.append('')
            genre_list.append('')
            number_of_ratings_list.append('')
            number_of_reviews_list.append('')
            page_list.append('')
            places_list.append('')
            publish_year_list.append('')
            titles_list.append('')
            series_list.append('')
        print(author_list[-1],page_list[-1])
    Data = pd.DataFrame(data={'URL': urls,
                              'Title': titles_list,
                              'Author': author_list,
                              'Number of reviews': number_of_reviews_list,
                              'Number of ratings': number_of_ratings_list,
                              'Average rating': avg_rating_list,
                              'Pages': page_list,
                              'Publish year': publish_year_list,
                              'Series': series_list,
                              'Genres': genre_list,
                              'Awards': award_list,
                              'Places': places_list})
    Data.to_csv('Data.csv')
scraper()