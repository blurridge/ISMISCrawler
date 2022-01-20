# This script will enable us to scrape our grades without opening the ISMIS website.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import getpass
import os

def getUserInput(prompt,maximumNumber=None):
    if prompt == "What is your username?":
        if maximumNumber is not None:
            while True:
                userInput = input(prompt + "\n")
                if(len(userInput) < maximumNumber):
                    return userInput
                print("Invalid Input. Username is over 10 characters")
    elif prompt == "What is your password?":
        return getpass.getpass("What is your password?")

options = Options()
options.headless = True # Enables Chromium browser to run without being visible
ser = Service("/Users/blurridge/Documents/Coding/ISMISCrawler/chromedriver")
browser = webdriver.Chrome(service = ser, options = options)

clear = lambda: os.system('clear') # Clears the terminal

usernameInput = getUserInput("What is your username?", 10)
clear()
passwordInput = getUserInput("What is your password?", None) # Censors password entry
clear()

browser.get("https://ismis.usc.edu.ph")
username = browser.find_element(By.ID, "Username")
password = browser.find_element(By.ID, "Password")
loginButton = browser.find_element(By.CSS_SELECTOR, "button.btn")
print("Entering username...")
username.send_keys(usernameInput)
time.sleep(1)
print("Entering password...")
password.send_keys(passwordInput)
time.sleep(1)
print(f"Attempting login for {usernameInput}...")
loginButton.click()
print("Entering home page...")
time.sleep(5)

print("Navigating to grades page...")
browser.get("https://ismis.usc.edu.ph/ViewGrades")

try:
    body = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    tables = body.find_elements(By.CLASS_NAME, "table")
    maxTables = len(tables)
    # Changes range value based on number of tables
    if(maxTables == 2):
        rangeValue = maxTables - 1
    else:
        rangeValue = maxTables - 2
    for tableIndex in range(rangeValue):
        courseCode = tables[tableIndex].find_elements(By.CLASS_NAME, "col-lg-3")
        courseName = tables[tableIndex].find_elements(By.CLASS_NAME, "col-lg-6")
        unitNum = tables[tableIndex].find_elements(By.CSS_SELECTOR, "td.hidden-xs")
        gradeValue = tables[tableIndex].find_elements(By.CSS_SELECTOR, "td.col-lg-1:not(.hidden-xs)")
        maxCourses = len(courseCode)
        gradeIndex = 0
        print("{:20s} {:60s} {:7s} {:4s} {:4s}".format("Course Code", "Course Name", "Units", "MG", "FG"))
        for index in range(maxCourses):
            print("{:20s} {:60s} {:7s} {:4s} {:4s}".format(courseCode[index].text, courseName[index].text, unitNum[index].text, gradeValue[gradeIndex].text, gradeValue[gradeIndex+1].text))
            gradeIndex+=2
        print("\n\n")

finally:
    print("DONE!")
    browser.quit()