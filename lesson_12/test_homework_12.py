import unittest
from datetime import date
from homework_12 import Human

class TestHuman(unittest.TestCase):

    def setUp(self):
        self.human = Human("Test", "User", date(2000, 1, 1), "Male")

    def test_initial_energy(self):
        self.assertEqual(self.human.energy, 100)

    def test_eat(self):
        self.human.energy = 95
        self.human.eat()
        self.assertEqual(self.human.energy, 100)

    def test_sleep(self):
        self.human.energy = 85
        self.human.sleep()
        self.assertEqual(self.human.energy, 95)

    def test_speak(self):
        self.human.energy = 5
        self.human.speak()
        self.assertEqual(self.human.energy, 0)

    def test_walk(self):
        self.human.energy = 5
        self.human.walk()
        self.assertEqual(self.human.energy, 0)

    def test_do_hw(self):

        self.human.energy = 100
        self.human.do_hw()
        self.assertEqual(self.human.energy, 10)

    def test_combined_actions(self):
        self.human.walk()
        self.human.speak()
        self.human.eat()
        self.assertEqual(self.human.energy, 90)

    def test_max_energy(self):
        human1 = Human("Test", "Test1", date(1995, 5, 15), "Female")
        human2 = Human("Check", "Check1", date(1988, 8, 20), "Male")

        human1.walk()
        human2.do_hw()

        people = [human1, human2]

        # Знаходження людини з найбільшим рівнем енергії
        max_energy_person = max(people, key=lambda person: person.energy)
        self.assertEqual(max_energy_person, human1)


if __name__ == "__main__":
    unittest.main()
