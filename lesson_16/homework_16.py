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

    def __init__(self, user_name: str, user_email: str, access_level: str, logcount: int = 0):
        self.__user_name = user_name
        self.__user_email = user_email
        self.__access_level = access_level
        self.__logcount = logcount

    def __str__(self):
        return f'Користувач: {self.__user_name}, Електронна пошта: {self.__user_email}, Рівень доступу: {self.__access_level}'

    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self.__access_level == other.__access_level
        return False

    def increment_logcount(self, amount: int = 1):
        self.__logcount += amount

    @property
    def logcount(self):
        return self.__logcount

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError('Name must be a string')
        self.__user_name = new_name

    @property
    def user_email(self):
        return self.__user_email

    @user_email.setter
    def user_email(self, new_email: str):
        if not isinstance(new_email, str):
            raise ValueError('Email must be a string')
        self.__user_email = new_email

    @property
    def access_level(self):
        return self.__access_level

    @access_level.setter
    def access_level(self, new_access: str):
        if not isinstance(new_access, str):
            raise ValueError('Access must be a string')
        elif new_access not in ['admin', 'moderator', 'user']:
            raise ValueError('There are only 3 access roles in a system: admin/moderator/user')
        self.__access_level = new_access


if __name__ == '__main__':
    serhii = SiteUser(user_name='Serhii', user_email='sobaka@gmail.com', access_level='user')
    ihor = SiteUser(user_name='Ihor', user_email='coteika@gmail.com', access_level='user')
    peter = SiteUser(user_name='Peter', user_email='spider@gmail.com', access_level='admin')

    print(f"Початкове значення logcount для serhii: {serhii.logcount}")
    serhii.increment_logcount()
    serhii.increment_logcount()
    print(f"Значення logcount для serhii після збільшення: {serhii.logcount}")

    ihor.increment_logcount(3)
    print(f"Значення logcount для ihor після збільшення на 3: {ihor.logcount}")

    if serhii == ihor:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")

    if serhii == peter:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")
