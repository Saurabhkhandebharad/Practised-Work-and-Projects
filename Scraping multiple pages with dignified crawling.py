import bs4
import requests
import io
from random import randint
from time import sleep

# Adding urls which are not serially indexed on the same webpage.
# taking examples from wikipedia

urls = [ 'https://en.wikipedia.org/wiki/Inception',
'https://en.wikipedia.org/wiki/Interstellar_(film)'
]

# adding personal user agent.
headers = {"User-Agent": " "}

#calling each url to be scraped in separate txt file.
for i, url in enumerate(urls):
    page = requests.get(url, headers=headers)
    tree = bs4.BeautifulSoup(page.text, 'lxml')

    title = tree.find('title').get_text()
    text = "".join([p.text for p in tree.find_all("p")])

    #adding names. We start from 1 as putting up file name from 0 gives headache afterwards.
    url_identifier = (urls.index(url)) + 1
    
    with io.open(f"{url_identifier}.txt" ,"w", encoding='utf-8') as text_file:
        text_file.write(title)
        text_file.write("\n")
        text_file.write(text)
        print('files are ready')

#adding sleeping time so website doesn't mistake us for bots
sleep(randint(2,10))        
