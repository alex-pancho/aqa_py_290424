from webelement import webelement, is_not_webelement


def test_example_with_explicit_wait(driver):
    driver.get("https://www.example.com")
    # Знаходимо елемент на сторінці
    heading = webelement(driver, '//h1', 10)  # .find_element(By.TAG_NAME, "h1")
    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"
    not_present = is_not_webelement(driver, '//h11', 1)  # наприклад, реклама що зникає для зареєст
    assert not_present, "Елемент продовжує бути на сторінці після очікування"
