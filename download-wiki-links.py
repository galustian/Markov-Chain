from bs4 import BeautifulSoup
import requests
import pickle

url = "https://en.wikipedia.org/wiki/User:SethAllen623/Vital_articles/Level/2"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")

top_500_links = soup.select("div[class^=div-col] a[href^=/wiki/]")
top_500_href = [link['href'] for link in top_500_links]

pickle.dump(top_500_href, open('wiki_links.p', 'wb'))
print(pickle.load(open('wiki_links.p', 'rb')))