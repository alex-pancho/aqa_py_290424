
# test_homework_16.py

import unittest
from homework_16 import SiteUser

class TestSiteUser(unittest.TestCase):

    def setUp(self):
        self.user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        self.user2 = SiteUser("Agent Smith", "agent.smith@example.com", "admin")
        self.user3 = SiteUser("Mr Andersen", "mr.andersen@example.com", "user")

    def test_initialization(self):
        self.assertEqual(self.user1.name, "John Doe")
        self.assertEqual(self.user1.email, "john.doe@example.com")
        self.assertEqual(self.user1.access_level, "user")
        self.assertEqual(self.user1.logcount, 0)

    def test_setters(self):
        self.user1.name = "Johnathan Doe"
        self.assertEqual(self.user1.name, "Johnathan Doe")

        self.user1.access_level = "moderator"
        self.assertEqual(self.user1.access_level, "moderator")

    def test_str_method(self):
        self.assertEqual(str(self.user1), "Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user")

    def test_eq_method(self):
        self.assertTrue(self.user1 == self.user3)
        self.assertFalse(self.user1 == self.user2)

    def test_increment_logcount(self):
        self.user1.increment_logcout()
        self.assertEqual(self.user1.logcount, 1)
        self.user1.increment_logcout()
        self.assertEqual(self.user1.logcount, 2)

if __name__ == "__main__":
    unittest.main()


