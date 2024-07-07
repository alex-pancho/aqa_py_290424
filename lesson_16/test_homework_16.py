import unittest
from homework_16 import SiteUser

class TestSiteUser(unittest.TestCase):

    def setUp(self):
        self.user1 = SiteUser("John Doe", "john.doe@email.com", "user")
        self.user2 = SiteUser("Jane Smith", "jane.sm@gmail.com", "admin")
        self.user3 = SiteUser("Mike Tyson", "mikee@gmail.com", "user")

    def test_init(self):
        self.assertEqual(self.user1.name, 'John Doe')
        self.assertEqual(self.user1.email, 'john.doe@email.com')
        self.assertEqual(self.user1.access_level, 'user')
        self.assertEqual(self.user1.logcount, 0)

    def test_increment_logcount(self):
        self.user1.increment_logcount()
        self.assertEqual(self.user1.logcount, 1)

    def test_str_method(self):
        expected_str = "Користувач: John Doe, Електронна пошта: john.doe@email.com, Рівень доступу: user"
        self.assertEqual(str(self.user1), expected_str)

    def test_eq_method(self):
        self.assertTrue(self.user1 != self.user2)  # Перевірка, що користувачі мають різний рівень доступу
        self.user1.access_level = "admin"
        self.assertTrue(self.user1 == self.user2)  # Перевірка, що користувачі мають однаковий рівень доступу

    def test_setters(self):
        self.user1.name = "John Doe Jr."
        self.assertEqual(self.user1.name, "John Doe Jr.")

        self.user1.access_level = "moderator"
        self.assertEqual(self.user1.access_level, "moderator")


if __name__ == "__main__":
    unittest.main()