from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver =  webdriver.Chrome()

driver.get("http://localhost:8000/dz.html")

# Функція для верифікації тексту у фреймі
def verify_frame(frame_id, input_id, secret_text):
    # Перехід до фрейму
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))
    
    # Введення секретного тексту
    input_element = driver.find_element(By.ID, input_id)
    input_element.send_keys(secret_text)
    
    # Натискання кнопки "Перевірити"
    button = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    button.click()
    
    # Очікування появи діалогового вікна
    time.sleep(1)
    
    # Перехід до діалогового вікна та отримання тексту
    alert = Alert(driver)
    alert_text = alert.text
    print(f"Alert text from {frame_id}: {alert_text}")
    
    # Закриття діалогового вікна
    alert.accept()
    
    # Повернення до основного контенту
    driver.switch_to.default_content()

# Верифікація тексту у фреймах
verify_frame("frame1", "input1", "Frame1_Secret")
verify_frame("frame2", "input2", "Frame2_Secret")

driver.quit()