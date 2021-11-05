from bs4 import BeautifulSoup
import requests

def yahooarticlews(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    article = soup.find("div", class_= "caas-body")
    print(soup.title.string)
    print(article.get_text())
    



url = 'https://finance.yahoo.com/news/stock-market-news-live-updates-october-8-2021-221828813.html'
yahooarticlews(url)

