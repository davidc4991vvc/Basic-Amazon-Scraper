from selenium import webdriver
from bs4 import BeautifulSoup
from collections import deque
from threading import Thread
from urllib.parse import urlsplit
import re

new_urls = deque([])
processed_urls = set()

#Starting URL List
URLs = ["https://www.amazon.co.uk/gp/product/B01HIWOOWM/","https://www.amazon.co.uk/ASUS-Zenbook-UX305CA-FB038T-13-3-Inch-Notebook/dp/B01HIWOOEU/",
        "https://www.amazon.co.uk/gp/product/B01IU8FL16/"]
for item in URLs:
    new_urls.append(item)

AmazonDomain = re.compile('https:\/\/www\.amazon\.co\.uk\/gp\/product\/.*')
ProductURL = re.compile('(.*\/gp\/product\/.*|.*\/dp\/.*)')
BannedPages = re.compile('(.*#.*|.*signin.*)')

def extractHTML():
    i = 0
    driver = webdriver.Chrome()
    while len(new_urls) > 0:
        url = new_urls.popleft()
        driver.get(url)
        html = driver.page_source
        fileName = 'htmlFile{}.html'.format(i)
        currentURL = driver.current_url
        if ProductURL.match(currentURL):
            with open(fileName,'w',encoding='utf-8') as htmlfile:
                htmlfile.write(html)
                i += 1
        else:
            pass
        soup = BeautifulSoup(html,'html.parser')

        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        for anchor in soup.find_all("a"):
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link

            if AmazonDomain.match(link) and not BannedPages.match(link):
                if not link in new_urls and not link in processed_urls:
                    new_urls.append(link)

for i in range(3):
    t1 = Thread(target=extractHTML)
    t1.start()