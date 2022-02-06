import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('C:\\Users\\DELL\\PycharmProjects\\welcome\\web_page.html')

FirstName = driver.find_element(By.NAME, "fname")
FirstName.send_keys("simarjeet123")

LastName = driver.find_element(By.ID, "345")
LastName.send_keys("kaur kaur kaur")
PhoneNum = driver.find_element(By.ID, "567")
PhoneNum.send_keys("514888999912345")
Country = driver.find_element(By.NAME, "cun")
Country.send_keys("canada")
City = driver.find_element(By.NAME, "city")
City.send_keys("montreal")
PostalCode = driver.find_element(By.NAME, "pc")
PostalCode.send_keys("h8n1p1")
time.sleep(3)


# ============================================================== #

def measureTextBox(object):
    value = object.get_attribute('value')
    return len(value)


def test_fname():
    assert 10 == measureTextBox(FirstName)


def test_lname():
    assert 10 == measureTextBox(LastName)


def test_pnum():
    assert 10 == measureTextBox(PhoneNum)


def test_country():
    assert measureTextBox(Country) <= 10


def test_city():
    assert measureTextBox(City) <= 10


def test_pcode():
    assert measureTextBox(PostalCode) <= 10
