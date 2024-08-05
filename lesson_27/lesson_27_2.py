from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()


def action_and_frame():
    driver.get("http://localhost/action.html")

    # Знаходження текстових полів за ID і введення тексту
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("example_username")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("example_password")

    # Знаходження радіо кнопок за ID і вибір варіанта
    male_radio = driver.find_element(By.ID, "male")
    male_radio.click()

    # Знаходження чекбоксу за ID і встановлення прапорця
    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    newsletter_checkbox.click()

    # Вибір значення з випадаючого списку за ID
    country_dropdown = Select(driver.find_element(By.ID, "country"))
    country_dropdown.select_by_visible_text("США")

    # Натискання на кнопку за ID
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # # Зачекати 5 секунд перед завершенням
    # time.sleep(5)
    driver.get("http://localhost/frame.html")

    # Прокрутка вниз
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Зачекайте трохи після прокрутки вниз

    # Прокрутка вгору
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)  # Зачекайте трохи після прокрутки вгору


    # Перемикаємося до фрейму
    driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))

    # Вибір значення з випадаючого списку за ID
    country_dropdown = Select(driver.find_element(By.ID, "country"))
    country_dropdown.select_by_visible_text("США")

    time.sleep(1)

def alert_show():
    driver.get("http://localhost/alert.html")

    # Показати Alert і отримати текст з нього
    driver.find_element(By.XPATH, "//button[text()='Показати Alert']").click()
    alert = Alert(driver)
    print("Текст Alert:", alert.text)
    alert.accept()

    # Показати Confirm і підтвердити його
    driver.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
    alert = Alert(driver)
    print("Текст Confirm:", alert.text)
    alert.accept()

    # Показати Prompt, ввести текст і підтвердити його
    driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
    alert = Alert(driver)
    print("Текст Prompt:", alert.text)
    alert.send_keys("John")
    alert.accept()

    # Зачекати 2 секунди перед завершенням
    time.sleep(2)

alert_show()
