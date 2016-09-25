# Basic-Amazon-Scraper
Basic Amazon scraper using Python, Selenium and placing info into a SQLite database

The Scraper uses Selenium and threading to scrape product pages from the Amazon.co.uk website. 
The HTML of these pages is downloaded to a users hard drive, with the extract HTML file - using BS4 to add information to a SQLite database.
This short project was primarily to play around with Selenium and Python multi-threading, which works surprisingly well. 
Also wanted to experiment with splitting up different parts of the process to achieve better concurrency.
