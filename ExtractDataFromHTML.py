import glob, os, sqlite3
from time import sleep
from bs4 import BeautifulSoup

try:
    conn = sqlite3.connect('ProductDatabase.db')
    conn.execute('''CREATE TABLE PRODUCTS(ProductTitle TEXT PRIMARY KEY NOT NULL,Price TEXT,Rating TEXT);''')
    conn.close()
except:
    print('Table Created')



for item in glob.glob('*.html'):
    try:
        with open(item,'r') as htmlfile:
            soup = BeautifulSoup(htmlfile,'html.parser')
    except:
        pass
    try:
        ProductTitle = soup.find('span',attrs={'id':'productTitle'}).text
    except:
        ProductTitle = "Missing"
    try:
        OurPrice = soup.find('span',attrs={'id':'priceblock_ourprice'}).text
    except:
        OurPrice = "None"
    try:
        soup2 = soup.find('i',attrs={'class':'a-icon-star'})
        Rating = soup2.find('span',attrs={'class':'a-icon-alt'}).text
    except:
        Rating = "None"
    try:
        if ProductTitle == "Missing":
            pass
        else:
            conn = sqlite3.connect('ProductDatabase.db')
            conn.execute('''INSERT OR REPLACE INTO PRODUCTS (ProductTitle,Price,Rating)
            VALUES(?,?,?)''', (ProductTitle.strip(), OurPrice.strip(), Rating.strip()))
            conn.commit()
            conn.close()
    except:
        pass
    try:
        os.remove(item)
    except:
        pass