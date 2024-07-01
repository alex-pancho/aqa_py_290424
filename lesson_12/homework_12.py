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
eating_cost = -5
sleeping_cost = -10
talking_cost = 5
walking_cost = 10
doing_homework_cost = 90
class Human:
    energy_level = 100
    def __init__(self, name: str, surname: str, birthdate: str, gender: str) -> None:
        self.name = name
        self.surname = surname
        self.bitrhdate = birthdate
        self.gender = gender

    def basic_action(self, energy_cost: int, action: str):
        energy_level_result = self.energy_level - energy_cost
        if energy_level_result > 0:
            self.energy_level = energy_level_result
            print(f'{self.name} is currently {action}. Energy level update: {self.energy_level}')
        else:
            print("Energy level is too low to perform this action.")

    def eat(self):
        self.basic_action(eating_cost, "eating")

    def sleep(self):
        self.basic_action(sleeping_cost, "sleeping")

    def talk(self):
        self.basic_action(talking_cost, "talking")

    def walk(self):
        self.basic_action(walking_cost, "walking")

    def do_homework(self):
        self.basic_action(doing_homework_cost, "doing homework")

def max_energy_level(*humans):
    temp_max_energy = -1
    temp_name = ""
    for human in humans:
        if human.energy_level > temp_max_energy:
            temp_max_energy = human.energy_level
            temp_name = human.name

    print(f"{temp_name} has maximum energy level")


if __name__ == "__main__":
    bob = Human("Bob", "Blahblah", "December 31st", "male")
    bob.eat()
    bob.sleep()
    bob.do_homework()

    john = Human("John", "Peterson", "January 2nd", "male")
    john.talk()
    john.do_homework()
    john.sleep()

    mark = Human("Mark", "Yeppi", "March 15th", "male")
    mark.walk()
    mark.talk()
    mark.eat()

    lara = Human("Lara", "Lala", "July 27th", "female")
    lara.talk()
    lara.walk()
    lara.do_homework()
    lara.eat()

    maria = Human("Maria", "Vele", "October 21st", "female")
    maria.do_homework()
    maria.sleep()
    maria.eat()
    maria.walk()
    maria.walk()

max_energy_level(bob, john, mark, lara, maria)
