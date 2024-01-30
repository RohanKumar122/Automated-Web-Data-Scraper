from selenium import webdriver
from bs4 import BeautifulSoup
from database_connection import *

def sitemap_crawler(sitemap_url):
    driver = webdriver.Chrome()
    driver.get(sitemap_url)
    sitemap_xml = driver.page_source
    driver.quit()
    soup = BeautifulSoup(sitemap_xml, 'html.parser')
    links = soup.find_all('loc')
    print(f"Total {len(links)} links found in Sitemap")
    for link in links :
        link_collection.insert_one({"url":link.text.strip(), "Scrapped": False})

    print("All links insereted in Database")

sitemap_url = "https://indianexpress.com/news-sitemap.xml"
sitemap_crawler(sitemap_url)