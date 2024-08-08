from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def webelement(driver: webdriver, xpath: str, timeout: int = 5):
    try:
        element = WebDriverWait(driver, timeout=timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        print("За даний час елемент не зявився на сторінці")


def is_not_webelement(driver: webdriver, xpath: str, timeout: int = 2):
    try:
        element = WebDriverWait(driver, timeout=timeout).until_not(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return True
    except TimeoutException:
        print("Елемент продовжує бути на сторінці після очікування")
        return False
