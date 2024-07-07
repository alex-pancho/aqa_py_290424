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


class SiteUser():
    def __init__(self, name, email, access_level):
        self.name = name
        self.email = email
        self.access_level = access_level
        self.logcount = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property

    def access_level(self):
        return self._access_level

    @property

    def logcount(self):
        return self._logcount

    @logcount.setter
    def logcount(self, new_logcount):
        self._logcount = new_logcount

    @access_level.setter
    def access_level(self, new_access_level):
        self._access_level = new_access_level

    def increment_logcount(self):
        self._logcount += 1

    def __str__(self):
        return f"Користувач: {self._name}, Електронна пошта: {self._email}, Рівень доступу: {self._access_level}"

    def __eq__(self, other):
        return self._access_level == other._access_level


user1 = SiteUser("John Doe", "john.doe@gmail.com",'user')
user2 = SiteUser("Jane Smith", "janesmt@gmail.com", "admin")

print(user1)
print(user2)

user1.increment_logcount()
print(f"Лічильник логінів користувача {user1.name}: {user1.logcount}")

if user1 == user2:
    print("Користувачі однакові")
else:
    print("У користувачів різні рівні доступів")




