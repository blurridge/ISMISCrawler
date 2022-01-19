# This script will enable us to scrape our grades without opening the ISMIS website.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

ser = Service("/Users/blurridge/Documents/Coding/ISMISCrawler/chromedriver")
browser = webdriver.Chrome(service = ser)

browser.get("file:///Users/blurridge/Documents/Coding/ISMISCrawler/testScrape.html")

try:
    body = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    tables = body.find_elements(By.CLASS_NAME, "table")
    maxTables = len(tables)
    for tableIndex in range(maxTables - 1):
        courseCode = tables[tableIndex].find_elements(By.CLASS_NAME, "col-lg-3")
        courseName = tables[tableIndex].find_elements(By.CLASS_NAME, "col-lg-6")
        unitNum = tables[tableIndex].find_elements(By.CSS_SELECTOR, "td.hidden-xs")
        gradeValue = tables[tableIndex].find_elements(By.CSS_SELECTOR, "td.col-lg-1:not(.hidden-xs)")
        maxCourses = len(courseCode)
        gradeIndex = 0
        print("{:20s} {:40s} {:7s} {:4s} {:4s}".format("Course Code", "Course Name", "Units", "MG", "FG"))
        for index in range(maxCourses):
            print("{:20s} {:40s} {:7s} {:4s} {:4s}".format(courseCode[index].text, courseName[index].text, unitNum[index].text, gradeValue[gradeIndex].text, gradeValue[gradeIndex+1].text))
            gradeIndex+=2
        print("\n\n")

finally:
    print("DONE!")
    browser.quit()