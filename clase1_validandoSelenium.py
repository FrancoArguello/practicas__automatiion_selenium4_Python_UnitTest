import os
from selenium import webdriver

os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("http://python.org")
driver.close()