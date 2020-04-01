#!/usr/bin/env python3
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
import time

driver = webdriver.Chrome()

START_PAGE = 7
END_PAGE = 368
PAGE_OFFSET = -1
BASE_URL = 'http://www.nayiri.com/imagedDictionaryBrowser.jsp?dictionaryId=21&pageNumber='

# Iteratively save dictionary pages in a directory
for i in range(START_PAGE, END_PAGE + 1):

    # Generate and visit URL
    url = BASE_URL + str(i + PAGE_OFFSET)
    driver.get(url)

    # Locate image
    img = driver.find_element_by_id('pageImage')

    # Right-click
    actionChains = ActionChains(driver)
    actionChains.context_click(img).perform()

    # Navigate to 'Save Image As...'
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(2)

    # Enumerate file with leading zeros and save
    pyautogui.write(str(i).zfill(3))
    time.sleep(1)
    pyautogui.press('enter')

driver.close()
