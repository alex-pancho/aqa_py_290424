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

BASE_URL = "https://petstore.swagger.io/v2"

def get_all_pets():
    url = f"{BASE_URL}/pet/findByStatus"
    params = {'status': 'available,pending,sold'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        all_pets = response.json()
        print("Список усіх доступних тварин:")
        for pet in all_pets:
            name = pet.get('name', 'Без імені')
            print(f"ID: {pet['id']}, Ім'я: {name}, Статус: {pet['status']}")
        return all_pets
    else:
        print(f"Помилка отримання списку всіх тварин: {response.status_code} - {response.text}")
        return None

def get_pets_by_status(statuses):
    url = f"{BASE_URL}/pet/findByStatus"
    params = {'status': ','.join(statuses)}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        pets = response.json()
        print(f"Список тварин зі статусами {statuses}:")
        for pet in pets:
            name = pet.get('name', 'Без імені')
            print(f"ID: {pet['id']}, Ім'я: {name}, Статус: {pet['status']}")
        return pets
    else:
        print(f"Помилка отримання списку тварин: {response.status_code} - {response.text}")
        return None

def add_pet(name, status):
    url = f"{BASE_URL}/pet"
    pet_data = {
        "id": 0,
        "name": name,
        "status": status
    }
    response = requests.post(url, json=pet_data)
    if response.status_code == 200 or response.status_code == 201:
        pet = response.json()
        print(f"Додано нову тварину: ID: {pet['id']}, Ім'я: {pet['name']}, Статус: {pet['status']}")
        return pet['id']
    else:
        print(f"Помилка додавання тварини: {response.status_code} - {response.text}")
        return None

def get_pet_by_id(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    if response.status_code == 200:
        pet = response.json()
        name = pet.get('name', 'Без імені')
        print(f"Знайдено тварину: ID: {pet['id']}, Ім'я: {name}, Статус: {pet['status']}")
        return pet
    else:
        print(f"Помилка пошуку тварини за ID: {response.status_code} - {response.text}")
        return None

def delete_pet_by_id(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Тварину з ID {pet_id} видалено успішно.")
        return True
    else:
        print(f"Помилка видалення тварини: {response.status_code} - {response.text}")
        return False

# Виклики функцій для тестування

# Отримати список доступних тварин зі статусами "available", "pending" та "sold"
all_pets = get_pets_by_status(["available", "pending", "sold"])

# Додати нову тварину та отримати її ID
new_pet_id = add_pet("Pushok", "available")

if new_pet_id:
    # Знайти тварину за ідентифікатором
    pet = get_pet_by_id(new_pet_id)

    # Видалити тварину за ідентифікатором
    deleted = delete_pet_by_id(new_pet_id)
