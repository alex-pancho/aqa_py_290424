from datetime import date
class Human:
    def __init__(self, name, surname, birthdate, gender):
        """
        Init for Human: name, surname, birthdate, gender, energy
        """
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.energy = 100
    def eat(self):
        self.energy += 5
        if self.energy > 100:
            self.energy = 100
    def sleep(self):
        self.energy += 10
        if self.energy > 100:
            self.energy = 100
    def speak(self):
        self.energy -= 5
        if self.energy < 0:
            self.energy = 0
    def walk(self):
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0
    def do_hw(self):
        self.energy -= 90
        if self.energy < 0:
            self.energy = 0
    def __repr__(self):
        return f"{self.name} {self.surname} with energy {self.energy}"

if __name__ == "__main__":
    oleksandr = Human("Oleksandr", "Panchenko", date(1980, 1, 1), "Male")
    mike = Human("Mike", "Rilskyi", date(1995, 2, 2), "Male")
    illya = Human("Illya", "Nechutaylo", date(2000, 3, 3), "Male")
    karyna = Human("Karyna", "Tashchi", date(1995, 6, 27), "Female")
    bohdana = Human("Bohdana", "Yuich", date(1980, 5, 5), "Female")

    # Виконання дій
    oleksandr.walk()
    oleksandr.speak()
    oleksandr.eat()

    mike.sleep()
    mike.do_hw()

    illya.do_hw()
    illya.eat()

    karyna.speak()
    karyna.walk()
    karyna.sleep()
    karyna.do_hw()

    bohdana.speak()
    bohdana.eat()
    bohdana.do_hw()

    people = [oleksandr, mike, illya, karyna, bohdana]

    # Окрема функція для отримання рівня енергії
    def get_energy(person):
        return person.energy

    # Знаходження людини з найбільшим рівнем енергії
    max_energy_person = max(people, key=get_energy)
    print(f"Person with most energy is: {max_energy_person}")


