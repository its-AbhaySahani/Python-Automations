import requests
from bs4 import BeautifulSoup


def scrape_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find('title').get_text()
        
        return title
    else:
        return None

url = 'https://www.geeksforgeeks.org/data-structures/'
title = scrape_title(url)
if title:
    print(f'Title of the page: {title}')
else:
    print('Failed to retrieve the page')
