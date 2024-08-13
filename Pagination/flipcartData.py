import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for the Flipkart search results page
base_url = 'https://www.flipkart.com/search?q=smartphones'

# Initialize empty lists to store the scraped data
product_names = []
product_prices = []
product_ratings = []
product_reviews = []

# Function to scrape the Flipkart page
def scrape_flipkart(page_number):
    url = f"{base_url}&page={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all product containers
    product_containers = soup.findAll("div", {"class": "_1AtVbE"})
    
    for container in product_containers:
        # Scrape product name
        name = container.find("a", {"class": "IRpwTa"})
        if not name:  # Try another class if first fails
            name = container.find("div", {"class": "_4rR01T"})
        if name:
            product_names.append(name.text)
        else:
            product_names.append("N/A")
        
        # Scrape product price
        price = container.find("div", {"class": "_30jeq3 _1_WHN1"})
        if price:
            product_prices.append(price.text)
        else:
            product_prices.append("N/A")
        
        # Scrape product rating
        rating = container.find("div", {"class": "_3LWZlK"})
        if rating:
            product_ratings.append(rating.text)
        else:
            product_ratings.append("N/A")
        
        # Scrape number of reviews
        reviews = container.find("span", {"class": "_2_R_DZ"})
        if reviews:
            review_text = reviews.text.split('&')[0].strip()
            product_reviews.append(review_text)
        else:
            product_reviews.append("N/A")


for page in range(1, 6):  
    scrape_flipkart(page)


data = {
    'Product_Name': product_names,
    'Product_Price': product_prices,
    'Product_Rating': product_ratings,
    'Product_Reviews': product_reviews
}
df = pd.DataFrame(data, columns=['Product_Name', 'Product_Price', 'Product_Rating', 'Product_Reviews'])


df.to_csv('Flipkart_Products.csv', index=False)

print("Data has been successfully scraped and saved to Flipkart_Products.csv")
