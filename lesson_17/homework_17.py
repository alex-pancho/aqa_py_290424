"""
Ромбовидне наслідування

### Опис

Створіть клас **`Employee`**, який має атрибути **`name`** та **`salary`**.
Далі створіть два класи, **`Manager`** та **`Developer`**, які успадковуються від **`Employee`**.
Клас **`Manager`** повинен мати додатковий атрибут **`department`**, а клас **`Developer`** -
атрибут **`programming_language`**.

Тепер створіть клас **`TeamLead`**, який успадковується як від **`Manager`**, так і від **`Developer`**.
Цей клас представляє керівника з команди розробників. Клас **`TeamLead`** повинен мати всі атрибути як
**`Manager`** (ім'я, зарплата, відділ), а також атрибут **`team_size`**, який вказує на кількість розробників
у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрібутів з `Manager` та `Developer` у класі `TeamLead`

### Складність

Висока

# Як робити домашне завдання у Git

1. **ОБОВ’ЯЗКОВО с**творіть нову гілку, яка буде використовуватись для змін, за 
    допомогою команди `git checkout -b homework##`
2. **Виконайте ДЗ у окремому файлі homework_<#lesson>.py**
3. Зробіть коміт з змінами, додавши опис виконаних змін
4. Відправте свої зміни до вашого репозиторію 
5. Створіть pull request у  власну гілку `main` на головний репозиторію 
    [https://github.com](https://github.com/), натиснувши кнопку "New pull request" на
    відповідному розділі репозиторію.
6. Назначте ревьювером викладача
7. **Посилання на PR вставте у форму відповіді для ДЗ в навчальній системі**
"""

class Employe:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

class Manager(Employe):
    def __init__(self, name: str, salary: int, department: str):
        Employe.__init__(self, name, salary)
        self.department = department

class Developer(Employe):
    def __init__(self, name: str, salary: int, programming_language: str):
        Employe.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name: str, salary: int, department: str, programming_language: str, team_size: int):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size
