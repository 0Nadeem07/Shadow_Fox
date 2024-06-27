import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_soup(url):
    response = requests.get(url)
    time.sleep(10)  # Adding a delay to be gentle with the website
    return BeautifulSoup(response.content, 'html.parser')

def scrape_products(url):
    base_url = "https://www.boat-lifestyle.com"
    soup = get_soup(url)
    container = soup.find('div', id='Huratips_Loop')
    
    product_name = []
    product_link = []
    product_price = []
    product_description = []
    star_rating = []
    
    names = container.find_all('a', class_='product-item-meta__title tile-title')
    for name in names:
        product_name.append(name.text.strip())
        link = base_url + name['href']
        product_link.append(link)
    
    prices = container.find_all('span', class_='price price--highlight product-card-price')
    for price in prices:
        product_price.append(price.text.strip()[11:])
    
    details = container.find_all('div', class_='features-list only-horizontal')
    span_desc = container.find_all('span', class_='metafeild-label label--highlight custom-label label ui-2')
    
    for i, detail in enumerate(details):
        span_list = [span.text.strip() for span in detail.find_all('span')]
        span_list.append(span_desc[i].text.strip())
        product_description.append(span_list)
    
    containers = soup.find_all('div', class_='rating')
    for container in containers:
        star = container.find('div', class_='rating__stars').text.strip()
        star_rating.append(star)
    
    return product_name, product_link, product_price, product_description, star_rating

def create_dataframe(product_name, product_link, product_price, product_description, star_rating):
    df = pd.DataFrame({
        'product_name': product_name,
        'product_link': product_link,
        'product_price': product_price,
        'product_rating': star_rating,
        'product_description': product_description
    })
    return df

def main():
    url = "https://www.boat-lifestyle.com/collections/true-wireless-earbuds"
    product_name, product_link, product_price, product_description, star_rating = scrape_products(url)
    df = create_dataframe(product_name, product_link, product_price, product_description, star_rating)
    print(df)
    df.to_excel('boat_data.xlsx', index=False)

if __name__ == "__main__":
    main()
