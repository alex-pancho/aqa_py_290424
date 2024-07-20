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
import json
from func_request import make_get_request, make_post_request, make_delete_request
from template import add_new_pet_request_body_template


URL = 'https://petstore.swagger.io/v2'
endpoint_find_pet_by_status = '/pet/findByStatus'
endpoint_pet = '/pet'
params_available_status = {'status': 'available'}


if __name__ == '__main__':
    # 1. Отримати список доступних тварин (метод GET).
    available_pets_response = make_get_request(url=URL, endpoint=endpoint_find_pet_by_status, params=params_available_status)
    available_pets_pretty_json = json.dumps(available_pets_response, indent=4, ensure_ascii=False)
    print(f'\n1. Список доступных животных: {available_pets_pretty_json}')

    # 2. Додати нову тварину (метод POST).
    new_pet_request_body = add_new_pet_request_body_template()
    add_new_pet_response = make_post_request(url=URL, endpoint=endpoint_pet, body=new_pet_request_body)
    add_new_pet_pretty_json = json.dumps(add_new_pet_response, indent=4, ensure_ascii=False)
    print(f'\n2. Добавление нового животного (ответ): {add_new_pet_pretty_json}')

    # 3. Знайти тварину за ідентифікатором (метод GET)
    find_pet_by_id_url = URL + endpoint_pet + '/' + str(add_new_pet_response['id'])
    get_pet_by_id_response = make_get_request(full_url=find_pet_by_id_url)
    get_pet_by_id_pretty_json = json.dumps(get_pet_by_id_response, indent=4, ensure_ascii=False)
    print(f'\n3. Нашли добавленное животное по id: {get_pet_by_id_pretty_json}')

    # 4. Видалити тварину за ідентифікатором (метод DELETE)
    delete_pet_by_id_url = find_pet_by_id_url
    delete_pet_by_id_response = make_delete_request(full_url=delete_pet_by_id_url)
    delete_pet_by_id_pretty_json = json.dumps(delete_pet_by_id_response, indent=4, ensure_ascii=False)
    print(f'\n4. Удалили добавленное животное по id: {delete_pet_by_id_pretty_json}')
