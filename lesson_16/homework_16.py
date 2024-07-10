"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран 
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = Користувач("John Doe", "john.doe@example.com", "user")
user2 = Користувач("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести
"""

class SiteUser:
    def __init__(self, name, email, permission, logcount=0):
        self._name = name
        self._email = email
        self._permission = permission
        self._logcount = logcount

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def permission(self):
        return self._permission

    @property
    def logcount(self):
        return self._logcount

    # Setters
    @name.setter
    def name(self, value):
        self._name = value

    @email.setter
    def email(self, value):
        self._email = value

    @permission.setter
    def permission(self, value):
        self._permission = value

    @logcount.setter
    def logcount(self, value):
        self._logcount = value

    
    def increment_logcount(self):
        self._logcount += 1

    
    def __str__(self):
        return f"Користувач: {self._name}, Електронна пошта: {self._email}, Рівень доступу: {self._permission}"

    
    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self._permission == other._permission
        return False


user_1 = SiteUser("John Doe", "john.doe@example.com", "user")
user_2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
print(user_1)  
print(user_2)  


if user_1 == user_2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")


print(user_1.logcount)
user_1.increment_logcount()
print(user_1.logcount)


import unittest

class TestSiteUser(unittest.TestCase):
    def test_initialization(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.permission, "user")
        self.assertEqual(user.logcount, 0)

    def test_setters(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        user.name = "Jane Doe"
        user.email = "jane.doe@example.com"
        user.permission = "admin"
        self.assertEqual(user.name, "Jane Doe")
        self.assertEqual(user.email, "jane.doe@example.com")
        self.assertEqual(user.permission, "admin")

    def test_increment_logcount(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        user.increment_logcount()
        self.assertEqual(user.logcount, 1)

    def test_str(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertEqual(str(user), "Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user")

    def test_eq(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", "user")
        user3 = SiteUser("Alice Johnson", "alice.johnson@example.com", "admin")
        self.assertTrue(user1 == user2)
        self.assertFalse(user1 == user3)

if __name__ == "__main__":
    unittest.main()