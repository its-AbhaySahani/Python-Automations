import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        paragraphs = soup.find_all('p')
        content = [p.get_text() for p in paragraphs]
        
        main_content = '\n'.join(content)
        
        return main_content
    else:
        return None

url = 'https://www.geeksforgeeks.org/data-structures/'
content = scrape_content(url)
if content:
    print(f'Content of the page:\n{content}')
else:
    print('Failed to retrieve the page')
