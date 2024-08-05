from selenium import webdriver
from selenium.webdriver.common.by import By
# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Firefox()

# Відкриття веб-сторінки
driver.get("http://localhost")

# Робота з веб-елементами і виконання дій на сторінці

# Закриття браузера
# driver.quit()

# Знаходження елемента за ID
user_field = driver.find_element(By.ID, "username")
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")
print(user_field.is_displayed())
print(pass_field.is_displayed())
print(login_button.is_displayed())

# Знаходження елемента за CSS класом
user_field = driver.find_element(By.CSS_SELECTOR, ".input-field#username")
pass_field = driver.find_element(By.CSS_SELECTOR, ".input-field#password")
login_button = driver.find_element(By.CSS_SELECTOR, "#login_button")
print(user_field.is_displayed())
print(pass_field.is_displayed())
print(login_button.is_displayed())

# Знаходження елемента за назвою тегу
form_element = driver.find_element(By.TAG_NAME, "form")
print(form_element.is_displayed())

# Знаходження елемента за XPath
user_field = driver.find_element(By.XPATH, "//input[@id='username']")
pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//button[@id='login_button']")
print(user_field.is_displayed())
print(pass_field.is_displayed())
print(login_button.is_displayed())

li_el2 = driver.find_element(By.XPATH, "//li[.='Елемент списку 2']")  # "//li[text()='Елемент списку 2']"
print(li_el2.is_displayed())
print(li_el2.text)
