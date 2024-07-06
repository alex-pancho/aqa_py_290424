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
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        # Employee.__init__(self, name, salary)
        super().__init__(**kwargs)
        self.team_size = team_size

team_lead = TeamLead(name="Опанас Заливаха", salary=1000, department="QA", programming_language="Python", team_size=7)

print(f"Ім'я тім ліда: {team_lead.name}")
print(f"Зарплата: {team_lead.salary}")
print(f"Департамент: {team_lead.department}")
print(f"Мова програмування: {team_lead.programming_language}")
print(f"Розмір команди: {team_lead.team_size}")
print(TeamLead.__mro__)


import unittest

class TestTeamLead(unittest.TestCase):
    def setUp(self):
        self.team_lead = TeamLead(name="Опанас Заливаха", salary=1000, department="QA", programming_language="Python", team_size=7)

    def test_attributes(self):
        self.assertEqual(self.team_lead.name, "Опанас Заливаха")
        self.assertEqual(self.team_lead.salary, 1000)
        self.assertEqual(self.team_lead.department, "QA")
        self.assertEqual(self.team_lead.programming_language, "Python")
        self.assertEqual(self.team_lead.team_size, 7)

if __name__ == "__main__":
    unittest.main(verbosity=2)