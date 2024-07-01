import unittest
from homework_16 import SiteUser

class TestSiteUser(unittest.TestCase):

    def setUp(self):
        self.user = SiteUser("Tetiana Suduk", "test@gmail.com", "moderator")

    def test_1_initialization(self):
        self.assertEqual(self.user.name, "Tetiana Suduk")
        self.assertEqual(self.user.email, "test@gmail.com")
        self.assertEqual(self.user.access_level, "moderator")
        self.assertEqual(self.user.logcount, 0)

    def test_2_getters_setters(self):
        self.user.name = "My Name"
        self.assertEqual(self.user.name, "My Name")

        self.user.email = "email@gmail.com"
        self.assertEqual(self.user.email, "email@gmail.com")

        self.user.access_level = "admin"
        self.assertEqual(self.user.access_level, "admin")

    def test_3_increment_logcount(self):
        self.user.increment_logcount()
        self.assertEqual(self.user.logcount, 1)
    
    def test_4_str_method(self):
        self.assertEqual(str(self.user), "User: Tetiana Suduk, Email: test@gmail.com, Access level: moderator")

    def test_5_eq_method(self):
        user1 = SiteUser("User1", "user1@gmail.com", "admin")
        user2 = SiteUser("User2", "user2@gmail.com", "admin")
        user3 = SiteUser("User3", "user3@gmail.com", "user")

        self.assertNotEqual(user1, user3)
        self.assertNotEqual(user2, user3)
        self.assertEqual(user1, user2)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)