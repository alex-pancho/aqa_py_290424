import unittest
from homework_16 import SiteUser

class TestSiteUser(unittest.TestCase):

    def test_user_initialization(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.access_level, "user")
        self.assertEqual(user.logcount, 0)

    def test_setters_and_getters(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        user.name = "Jane Doe"
        user.email = "jane.doe@example.com"
        user.access_level = "admin"
        self.assertEqual(user.name, "Jane Doe")
        self.assertEqual(user.email, "jane.doe@example.com")
        self.assertEqual(user.access_level, "admin")

    def test_str_method(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertEqual(str(user), "Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user")

    def test_equality(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", "user")
        user3 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertEqual(user1, user2)
        self.assertNotEqual(user1, user3)

    def test_increase_logcount(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        user.increase_logcount()
        self.assertEqual(user.logcount, 1)
        user.increase_logcount()
        self.assertEqual(user.logcount, 2)

if __name__ == "__main__":
    unittest.main()
