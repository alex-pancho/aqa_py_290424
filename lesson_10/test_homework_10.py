import unittest
from homework_10 import add_citizen, remove_citizen, add_resources, market_place, resources, imperial_citizens

class TestEmpireManagement(unittest.TestCase):

    def setUp(self):
        # Reset the initial state before each test
        self.initial_citizens = ["John", "Jane", "Bob", "Alice"]
        self.initial_resources = {"gold": 100, "wood": 50, "stone": 30}
        imperial_citizens.clear()
        imperial_citizens.extend(self.initial_citizens)
        resources.clear()
        resources.update(self.initial_resources)

    def test_add_citizen(self):
        add_citizen("Eve")
        self.assertIn("Eve", imperial_citizens)
        self.assertEqual(len(imperial_citizens), len(self.initial_citizens) + 1)

        with self.assertRaises(ValueError):
            add_citizen("John")

    def test_remove_citizen(self):
        remove_citizen("John")
        self.assertNotIn("John", imperial_citizens)
        self.assertEqual(len(imperial_citizens), len(self.initial_citizens) - 1)

        with self.assertRaises(ValueError):
            remove_citizen("NonExistent")

    def test_add_resources(self):
        add_resources("gold", 50)
        self.assertEqual(resources["gold"], self.initial_resources["gold"] + 50)

        add_resources("diamond", 10)
        self.assertIn("diamond", resources)
        self.assertEqual(resources["diamond"], 10)

    def test_market_place(self):
        market_place("stone", "gold")
        self.assertEqual(resources["stone"], self.initial_resources["stone"] - 5)
        self.assertEqual(resources["gold"], self.initial_resources["gold"] + 1)

        with self.assertRaises(ValueError):
            market_place("wood", "stone")

        resources["stone"] = 4
        with self.assertRaises(ValueError):
            market_place("stone", "gold")

if __name__ == '__main__':
    unittest.main()
