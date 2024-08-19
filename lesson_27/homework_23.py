from selenium import webdriver
from selenium.webdriver.common.by import By
import time


expected_text = "Верифікація пройшла успішно!"


def driver_chrome_initialisation():
    driver = webdriver.Chrome()
    return driver


def close_browser(driver):
    driver.quit()


def open_link(driver, link):
    driver.get(link)


def get_first_frame(browser_driver):
    browser_driver.switch_to.frame("frame1")

    first_frame_field = browser_driver.find_element(By.XPATH, "//input[@id='input1']")
    first_frame_field.send_keys("Frame1_Secret")
    first_frame_button = browser_driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")
    first_frame_button.click()

    alert = browser_driver.switch_to.alert
    alert_text_first = alert.text

    if alert_text_first == expected_text:
        print("Текст совпадает!")
    else:
        print(f"Текст не совпадает! Ожидалось: \'{expected_text}\', Получено: \'{alert_text_first}\'")

    time.sleep(3)

    alert.accept()

    browser_driver.switch_to.default_content()


def get_second_frame(browser_driver):
    browser_driver.switch_to.frame("frame2")

    second_frame_field = browser_driver.find_element(By.XPATH, "//input[@id='input2']")
    second_frame_field.send_keys("Frame_Secret")
    second_frame_button = browser_driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
    second_frame_button.click()

    alert = browser_driver.switch_to.alert
    alert_text_second = alert.text

    if alert_text_second == expected_text:
        print("Текст совпадает!")
    else:
        print(f"Текст не совпадает! Ожидалось: \'{expected_text}\', Получено: \'{alert_text_second}\'")

    time.sleep(3)

    alert.accept()

    browser_driver.switch_to.default_content()


if __name__ == '__main__':
    chrome_driver = driver_chrome_initialisation()
    open_link(chrome_driver, "http://localhost:8000/dz.html")
    time.sleep(3)
    get_first_frame(chrome_driver)
    time.sleep(3)
    get_second_frame(chrome_driver)
    time.sleep(3)
    close_browser(chrome_driver)
