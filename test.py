import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to get URL. Status code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_divs = soup.find_all("div", class_="quote")
    
    for i, quote_div in enumerate(quotes_divs):
        quote = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        print(f"Quote #{i+1}")
        print(f"  Quote: {quote}")
        print(f"  Author: {author}")
        print("---")

# Example usage
url = 'http://quotes.toscrape.com'
scrape_quotes(url)
