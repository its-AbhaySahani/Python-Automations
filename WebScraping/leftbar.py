import requests
from bs4 import BeautifulSoup

def scrape_left_sidebar(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        leftbar = soup.find('div', class_='leftbar')
        if leftbar:
            sidebar_content = leftbar.get_text(separator='\n')
            return sidebar_content
        else:
            return 'Left sidebar not found'
    else:
        return 'Failed to retrieve the page'

url = 'https://www.geeksforgeeks.org/python-programming-language-tutorial/'
sidebar_content = scrape_left_sidebar(url)
print(f'Left Sidebar Content:\n{sidebar_content}')
