# ISMIS Crawler by Zach Riane Machacon

## Context
Recently, I've been fascinated by the concept of webscraping using Python. Therefore, I will be using it to my advantage to solve my laziness by letting a script view my grades for me. 

## Current ideas
I'm planning to use Selenium through a headless Chromium webdriver to do authentication for me and accessing the grades URL itself. The grades are enclosed in tables which could be parsed by the script easily with a bit of experimentation.

## Progress report
January 19, 2021
- Managed to impelement authentication and scraping capability.
- Need to implement a catch function in case of site crash or incorrect credentials.

January 20, 2021
- Implemented checking for login status and site crash.
- Next plan would be to implement a checker for remaining balance for the semester.
