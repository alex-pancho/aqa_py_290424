"""
https://petstore.swagger.io/

Опис: Swagger Petstore - це відкрите API, яке надає можливість управляти даними про домашніх тварин. За допомогою цього API можна додавати нових тварин, знаходити тварин за ідентифікатором, виконувати замовлення на тварин та багато іншого.

Вам потрібно реалізувати програму, яка взаємодіє з Swagger Petstore API, використовуючи HTTP запити. Основні методи запитів, які вам знадобляться: GET, POST, PUT, DELETE.

**Ваші завдання:**

1. Отримати список доступних тварин (метод GET).

1. Зробіть запит до /pet/findByStatus з параметром status, щоб отримати список усіх тварин.

    1. Обробіть відповідь сервера та виведіть список тварин на екран.

1. Додати нову тварину (метод POST).

    Створіть новий об'єкт тварини з необхідною інформацією, наприклад, ім'я та статус.

    Зробіть запит до /pet з об'єктом тварини в тілі запиту, щоб додати нову тварину.

    Обробіть відповідь сервера та виведіть підтвердження про додавання тварини на екран.

1. Знайти тварину за ідентифікатором (метод GET).

    1. Введіть ідентифікатор тварини, яку потрібно знайти.

    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор шуканої тварини.

    1. Обробіть відповідь сервера та виведіть інформацію про знайдену тварину на екран.

1. Видалити тварину за ідентифікатором (метод DELETE).

    1. Введіть ідентифікатор тварини, яку потрібно видалити.

    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор тварини, яку потрібно видалити.

    1. Обробіть відпові
"""

import requests
import json


def animals_available(status="available"):
    url = "https://petstore.swagger.io/v2/pet/findByStatus"
    response = requests.get(url, params={"status": status})
    if response.status_code == 200:
        pets = response.json()
        for pet in pets:
            print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print(f"Failed to get. Status code: {response.status_code}")

def add_pet(name, status="available"):
    url = "https://petstore.swagger.io/v2/pet"
    pet = {
        "id": 0,
        "category": {"id": 0, "name": "string"},
        "name": name,
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": status
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(pet))
    if response.status_code == 200:
        print("Pet added")
    else:
        print(f"Failed to add. Status code: {response.status_code}")

def find_pet_id(pet_id):
    url = "https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.get(url)
    if response.status_code == 200:
        pet = response.json()
        print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print(f"Failed to find. Status code: {response.status_code}")

def delete_pet(pet_id):
    url = "https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Pet deleted")
    else:
        print(f"Failed to delete. Status code: {response.status_code}")


if __name__ == "__main__":
    animals_available("available")
    add_pet("Dog", "available")
    find_pet_id(1)
    delete_pet(1)



