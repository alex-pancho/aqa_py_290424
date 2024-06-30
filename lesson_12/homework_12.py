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
Створити тести на клас та на атрибути класу
"""

class Human:
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.energy = 100

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

    def __str__(self) -> str:
        return f"Human: {self.first_name}, {self.last_name}, {self.birth_date}, {self.gender}, {self.energy}" 

human_1 = Human("Vasyl", "Vasylenko", "11/01/91", "male")  
human_2 = Human("Gavryk", "Gavrychenko", "12/02/92", "male")
human_3 = Human("Mykola", "Mykolenko", "13/03/93", "male") 
human_4 = Human("Galyna", "Galychenko", "14/04/94", "female") 
human_5 = Human("Daryna", "Darychenko", "15/05/95", "female")  

human_1.eat()
human_1.sleep()
human_1.walk()

human_2.eat()
human_2.talk()
human_2.do_homework()

human_3.do_homework()
human_3.eat()
human_3.sleep()

human_4.eat()
human_4.talk()
human_4.sleep()

human_5.do_homework()
human_5.talk()
human_5.walk()

humans = [human_1, human_2, human_3, human_4, human_5]
most_energy_human = max(humans, key=lambda human: human.energy)
print(most_energy_human)

