import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def scrapeLinkedIn():
    load_dotenv()
    driver = webdriver.Chrome()
    # for selenium versions above 4.6, do NOT need to specify path to chrome driver. Selenium can handle it itself.

    driver.get("https://www.linkedin.com/login")

    # # wait for the page to load
    time.sleep(3)

    username = driver.find_element(By.ID, "username")
    # Enter MY Email Address, load from .env secure variables
    username.send_keys(os.environ.get("USERNAME")) 
    # print(os.environ.get("USERNAME"))
    password = driver.find_element(By.ID, "password")
    # Enter MY password, load from .env secure variables
    password.send_keys(os.environ.get['PW'])
    # find the button element and submit!!
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    

scrapeLinkedIn()