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
class Human():
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.energy = 100

    def eat(self):
        self.energy += 5

    def sleep(self):
        self.energy += 10

    def talk(self):
        self.energy -= 5

    def walk(self):
        self.energy -= 10

    def do_homework(self):
        self.energy -= 90

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, Energy: {self.energy}"

if __name__ == "__main__":
 
    man1 = Human("Lubomyr", "Andr", "1993-01-23", "Man")
    man2 = Human("Yaroslav", "Yar", "1993-06-16", "Man")
    man3 = Human("Dmytro", "Val", "1994-06-13", "Man")

    man1.eat()
    man1.talk()
    man1.sleep()

    man2.walk()
    man2.do_homework()

    man3.talk()
    man3.walk()
    man3.sleep()

    woman1 = Human("Victoria", "Vik", "2006-09-20", "Woman")
    woman2 = Human("Yana", "Ole", "1996-02-20", "Woman")
    
    woman1.eat()
    woman1.walk()
    woman1.do_homework()

    woman2.sleep()
    woman2.talk()

    people = [man1, man2, man3, woman1, woman2]

    """Пошук людини з найбільшою кількістю енергії"""
    most_energy = max(people, key=lambda person: person.energy)

    for person in people:
        print(person)

    print("The person with the most energy:", most_energy)


import unittest

class TestHuman(unittest.TestCase):
    def setUp(self):
        self.human = Human("Tetiana", "Suduk", "1998-04-11", "Woman")

    def test_01_initial_energy(self):
        self.assertEqual(self.human.energy, 100)

    def test_02_eat(self):
        self.human.eat()
        self.assertEqual(self.human.energy, 105)

    def test_03_sleep(self):
        self.human.sleep()
        self.assertEqual(self.human.energy, 110)

    def test_04_talk(self):
        self.human.talk()
        self.assertEqual(self.human.energy, 95)

    def test_05_walk(self):
        self.human.walk()
        self.assertEqual(self.human.energy, 90)

    def test_06_do_homework(self):
        self.human.do_homework()
        self.assertEqual(self.human.energy, 10)

    def test_07_full_name(self):
        self.assertEqual(f"{self.human.first_name} {self.human.last_name}", "Tetiana Suduk")

    def test_08_gender(self):
        self.assertEqual(self.human.gender, "Woman")

    def test_09_birth_date(self):
        self.assertEqual(self.human.birth_date, "1998-04-11")

    def test_10_str_method(self):
        self.assertEqual(str(self.human), "Tetiana Suduk, Woman, Energy: 100")


if __name__ == "__main__":
    unittest.main(verbosity=2)
