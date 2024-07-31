import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.example.com/product-reviews/B08N5WRWNW'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

reviews = []
for review in soup.find_all('div', class_='review'):
    title = review.find('a', class_='review-title').text.strip()
    rating = review.find('i', class_='review-rating').text.strip()
    text = review.find('span', class_='review-text').text.strip()
    reviews.append([title, rating, text])

df = pd.DataFrame(reviews, columns=['Title', 'Rating', 'Review'])
df.to_csv('product_reviews.csv', index=False)
