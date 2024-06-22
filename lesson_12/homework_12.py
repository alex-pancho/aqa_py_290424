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
    def __init__(self, first_name: str, second_name: str, birthday: str, sex: str, energy=100) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.birthday = birthday
        self.sex = sex
        self.energy = energy

    def __repr__(self) -> str:
        return f'My name is {self.first_name} {self.second_name} I am a {self.sex}. I was born in {self.birthday}'

    def to_eat(self):
        self.energy += 5

    def to_sleep(self):
        self.energy += 10

    def to_talk(self):
        self.energy -= 5

    def to_walk(self):
        self.energy -= 10

    def to_do_homework(self):
        self.energy -= 90

    @staticmethod
    def find_max_energy_person(people):
        maximum_energy_person = max(people, key=lambda person: person.energy)
        return maximum_energy_person


if __name__ == '__main__':
    # Создание экземпляров класса Human
    persons = [
        Human(first_name='Alex', second_name='Shevchenko', birthday='10.07.1986', sex='male'),
        Human(first_name='Oleg', second_name='Panasenko', birthday='06.11.1989', sex='male'),
        Human(first_name='Victor', second_name='Rozinskiy', birthday='05.03.1974', sex='male'),
        Human(first_name='Nastia', second_name='Melnichenko', birthday='17.09.1993', sex='female'),
        Human(first_name='Marina', second_name='Shapoval', birthday='13.12.1999', sex='female')
    ]
    # Вывод информации об экземплярах класса (с помощью магического метода __repr__)
    print(persons[0])  # Alex
    print(persons[1])  # Oleg
    print(persons[2])  # Victor
    print(persons[3])  # Nastia
    print(persons[4])  # Marina
    # Выполнение активностей
    persons[0].to_eat()
    persons[1].to_sleep()
    persons[2].to_talk()
    persons[3].to_walk()
    persons[4].to_do_homework()
    persons[0].to_walk()
    persons[1].to_do_homework()
    persons[2].to_walk()
    persons[3].to_talk()
    persons[4].to_eat()
    # Выводим на экран энергию наших экземпляров класса
    print(f'{persons[0].first_name} has {persons[0].energy} energy')
    print(f'{persons[1].first_name} has {persons[1].energy} energy')
    print(f'{persons[2].first_name} has {persons[2].energy} energy')
    print(f'{persons[3].first_name} has {persons[3].energy} energy')
    print(f'{persons[4].first_name} has {persons[4].energy} energy')
    # Ищем человека с наибольшей энергией
    max_energy_person = Human.find_max_energy_person(persons)
    print(f'{max_energy_person.first_name} has the most energy: {max_energy_person.energy}')
