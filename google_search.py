from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com/')
SearchBtn = driver.find_element(By.XPATH, "//html//body//div[1]//div[3]//form//div[1]"
                                          "//div[1]//div[1]//div//div[2]//input")
SearchBtn.send_keys("define computer")
SearchBtn.send_keys(Keys.ENTER)
time.sleep(2)

'''
(Sir i try to get the search result but i dont understand how to get and count the search result so i make this 
program upto this only)
results = driver.find_elements(By.XPATH, '//*[@id="gsr]')
for result in results:
    print(result.get_attribute("href"))
'''




