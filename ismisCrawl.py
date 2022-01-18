# This script will enable us to scrape our grades without opening the ISMIS website.

from selenium import webdriver

browser = webdriver.Chrome('/Users/blurridge/Documents/Coding/ISMISCrawler/chromedriver')

browser.get('https://ismis.usc.edu.ph/Account/Login')