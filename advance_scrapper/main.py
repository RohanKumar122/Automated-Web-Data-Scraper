from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import pymongo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from database_connection import *

def check(selector_type, driver, path):
    try: 
        selector = f"By.{selector_type}"
        driver.find_element(selector, path)
        print(f"Successfully find {path}") 
        return True
    except:
        print(f"Unable to find {path}") 
        return False

def wait_for_page_load(driver):
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    print("Page loaded successfully!")
        
def main():
    
    cursor = link_collection.find({}, {"url": 1}).limit(30)
    driver = webdriver.Chrome()

    for document in cursor:
        url = document["url"]
        driver.get(url)
        wait_for_page_load(driver)

        try :
            title_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,"title")))
            title = title_element.text
        except:
            title = ""

        try :
            post_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.storyDetails")))
            post = post_element.text
        except :
            post = ""

        try :    
            author_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.authorNameClick")))
            author = author_element.text
        except :
            author = ""

        try :    
            published_date_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.dateTime")))
            published_date = published_date_element.text
        except :
            published_date = ""
        

        dct = {"URL": url, "title": title, "post": post, "author": author, "published_date": published_date}

        try:
            data_collection.insert_one(dct)
            print(f"Data stored in Database : {dct}")
        except:
            print("Something went wrong with Database")


if __name__ == "__main__":
    main()