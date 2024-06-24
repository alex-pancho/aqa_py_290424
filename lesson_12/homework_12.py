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
    def __init__(self, first_name: str, last_name: str, birthday: str, sex: str, energy=100):
        """
        Init for Human:
        first_name
        last_name
        birthday
        sex
        energy
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex
        self.energy = energy

    def eat(self):
        self.energy += 5

    def sleep(self):
        self.energy += 10

    def talk(self):
        self.energy -= 5

    def walk(self):
        self.energy -= 10

    def do_homework(self):
        self.energy -= 90

@staticmethod

def find_person_with_max_energy(persons):
    max_energy_person = max(persons, key=lambda person: person.energy)
    return max_energy_person

if __name__ == '__main__':
    person1 = Human(first_name='Vadim', last_name='Ivanov', birthday='11.02.1999', sex='male')
    person2 = Human(first_name='Viktor', last_name='Ivanov', birthday='11.02.1978', sex='male')
    person3 = Human(first_name='Oleksii', last_name='Petrov', birthday='11.02.2001', sex='male')
    person4 = Human(first_name='Katya', last_name='Smirnina', birthday='11.02.1999', sex='female')
    person5 = Human(first_name='Elizaveta', last_name='Vokarchuk', birthday='11.02.1999', sex='female')

    person1.eat()
    person1.sleep()
    person1.talk()

    person2.walk()
    person2.do_homework()

    person3.eat()
    person3.walk()

    person4.sleep()
    person4.talk()

    person5.do_homework()
    person5.sleep()

    people = [person1 , person2, person3, person4, person5]
    max_energy_person = find_person_with_max_energy(people)

    print(f'Max energy person is {max_energy_person.first_name} {max_energy_person.last_name}, Energy of the person -> {max_energy_person.energy}')
