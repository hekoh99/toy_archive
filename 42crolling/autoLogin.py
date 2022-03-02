from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip

load_dotenv()

login_url = os.environ.get("login_url")
url = os.environ.get("url")
driver_path = os.environ.get("driver_path")

driver = webdriver.Chrome(driver_path)
driver.get(login_url)
time.sleep(1)

tag_id = driver.find_element_by_name('user[login]')
tag_pw = driver.find_element_by_name('user[password]')
tag_id.clear()
tag_pw.clear()
time.sleep(1)

USER = os.environ.get("USER")
PASS = os.environ.get("PASS")

tag_id.click()
pyperclip.copy(USER)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

tag_pw.click()
pyperclip.copy(PASS)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
session = requests.session()

login_btn = driver.find_element_by_name('commit')
login_btn.click()
time.sleep(3)

driver.get(url)
title = driver.find_element_by_tag_name('title').get_attribute('innerText')
print(title)
