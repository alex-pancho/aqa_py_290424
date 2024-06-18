"""Розробити клас Human.
Людина має:
    Ім'я
    Прізвище
    Дату народження
    Стать
    Енергію = 100
Люди можуть:
    Їсти (Енергія +5)
    Спати (Енергія +10)
    Говорити (Енергія -5)
    Ходити (Енергія -10)
    Робити домашку (Енергія -90)
if __name__ == "__main__":
    Створити 3 чоловіків та 2 жінок, Задати кожному з них виконання
    декількох дій, вивести в кого найбільше енергії лишилося.
Створити тести на клас та на атрибути класу.
"""


class Human:
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.energy = 100

    def eat(self):
        self.energy += 5
        print(f"{self.first_name} {self.last_name} їсть. Енергія тепер {self.energy}.")

    def sleep(self):
        self.energy += 10
        print(f"{self.first_name} {self.last_name} спить. Енергія тепер {self.energy}.")

    def talk(self):
        self.energy -= 5
        print(f"{self.first_name} {self.last_name} говорить. Енергія тепер {self.energy}.")

    def walk(self):
        self.energy -= 10
        print(f"{self.first_name} {self.last_name} ходить. Енергія тепер {self.energy}.")

    def do_homework(self):
        self.energy -= 90
        print(f"{self.first_name} {self.last_name} робить домашку. Енергія тепер {self.energy}.")

# створення піддослідних персон

if __name__ == "__main__":
    man1 = Human("Агент", "Сміт", "12.03.3496", "чоловік")
    man2 = Human("Андерсен", "Нео", "13.09.3449", "чоловік")
    man3 = Human("Батя", "Морфиус", "09.05.3455", "чоловік")
    woman1 = Human("Супер", "Тринити", "11.11.3111", "жінка")
    woman2 = Human("Мега", "Необа", "30.12.3696", "жінка")

# виконання дій

    man1.eat()
    man1.talk()
    man2.walk()
    man3.do_homework()
    woman2.walk()
    woman1.sleep()
    woman2.talk()

# список для перевірки енергії

    people = [man1, man2, man3, woman1, woman2]

# пошук людини з макс енегрією

    most_energetic = max(people, key=lambda person: person.energy)
    print(f"Найбільше енергії лишилося у {most_energetic.first_name} {most_energetic.last_name}: {most_energetic.energy}.")

import unittest

class TestHuman(unittest.TestCase):

    def setUp(self):
        self.human = Human("Тест", "Тестовий", "24.01.1999", "чоловік")

    def test_initial_energy(self):
        self.assertEqual(self.human.energy, 100)

    def test_eat(self):
        self.human.eat()
        self.assertEqual(self.human.energy, 105)

    def test_sleep(self):
        self.human.sleep()
        self.assertEqual(self.human.energy, 110)

    def test_talk(self):
        self.human.talk()
        self.assertEqual(self.human.energy, 95)

    def test_walk(self):
        self.human.walk()
        self.assertEqual(self.human.energy, 90)

    def test_do_homework(self):
        self.human.do_homework()
        self.assertEqual(self.human.energy, 10)

    def full_name(self):
        self.assertEqual(f"{self.human.first_name} {self.human.last_name}", "Тест Тестовий")

if __name__ == "__main__":
    unittest.main()
