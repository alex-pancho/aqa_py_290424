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
    def __init__ (self, name, surname, birth_date, gender, energy = 100):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
        self.energy = energy

    def eat(self):
        self.energy = self.energy + 5

    def sleep(self):
        self.energy = self.energy + 10

    def talk(self):
        self.energy = self.energy - 5

    def walk(self):
        self.energy = self.energy - 10

    def do_homework(self):
        self.energy = self.energy - 90

if __name__ == "__main__":
    man1 = Human("Sasha", "Petrenko", 1990, "M")
    man2 = Human("Petro", "Ivanov", 1980, "M")
    man3 = Human("Vadym", "Kozlyk", 1998, "M")
    woman1 = Human("Mariya", "Knopka", 1991, "F")
    woman2 = Human("Olena", "Solena", 2000, "F")
    man1.sleep()
    man1.eat()
    man1.do_homework()
    man2.walk()
    man3.do_homework()
    man3.eat()
    woman1.talk()
    woman2.talk()
    woman2.eat()
    people = [man1, man2, man3, woman1, woman2]
    max_e = max([i.energy for i in people])
    for i in people:
        if i.energy == max_e:
            print(f"The name of person with maximum energy is: {i.name} {i.surname}")

#Tests
import unittest


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.person = Human("Test", "User", 1984, "M")

    def test_initial_attributes(self):
        self.assertEqual(self.person.name, "Test")
        self.assertEqual(self.person.surname, "User")
        self.assertEqual(self.person.birth_date, 1984)
        self.assertEqual(self.person.gender, "M")
        self.assertEqual(self.person.energy, 100)

    def test_eat(self):
        self.person.eat()
        self.assertEqual(self.person.energy, 105)

    def test_sleep(self):
        self.person.sleep()
        self.assertEqual(self.person.energy, 110)

    def test_talk(self):
        self.person.talk()
        self.assertEqual(self.person.energy, 95)

    def test_walk(self):
        self.person.walk()
        self.assertEqual(self.person.energy, 90)

    def test_do_homework(self):
        self.person.do_homework()
        self.assertEqual(self.person.energy, 10)

    def test_multiple_actions(self):
        self.person.eat()
        self.person.walk()
        self.person.sleep()
        self.person.talk()
        self.assertEqual(self.person.energy, 100)

if __name__ == "__main__":
    unittest.main(verbosity=2)




