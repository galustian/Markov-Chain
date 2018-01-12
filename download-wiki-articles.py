import requests
from bs4 import BeautifulSoup
import pickle
import re
import os.path


top500_hrefs = pickle.load(open('wiki_links.p', 'rb'))

for i, href in enumerate(top500_hrefs):
    file_name = '{}.txt'.format(re.sub(r'\/(\w+)\/', '', href))
    file_name = file_name.replace('/', '_')
    file_name = 'wikipedia-articles/{}'.format(file_name)

    if os.path.isfile(file_name): continue

    req = requests.get("https://en.wikipedia.org" + href)
    soup = BeautifulSoup(req.text, 'lxml')
    
    paragraphs = soup.find_all('p')

    with open(file_name, 'w') as f:
        for p in paragraphs:
            clean_text = re.sub(r'\[(\d+)\]', '', p.text)
            f.write(clean_text + ' ')

    print("Downloading {}...".format(href), i, 'out of', len(top500_hrefs))