import pytest
from homework_12 import Human

def test_human_initialization():
    person = Human('John', 'Doe', '01.01.1990', 'male')
    assert person.first_name == 'John'
    assert person.last_name == 'Doe'
    assert person.birthday == '01.01.1990'
    assert person.sex == 'male'
    assert person.energy == 100

def test_human_eat():
    person = Human('John', 'Doe', '01.01.1990', 'male')
    person.eat()
    assert person.energy == 105

def test_human_sleep():
    person = Human('John', 'Doe', '01.01.1990', 'male')
    person.sleep()
    assert person.energy == 110

def test_human_talk():
    person = Human('John', 'Doe', '01.01.1990', 'male')
    person.talk()
    assert person.energy == 95

def test_human_walk():
    person = Human('John', 'Doe', '01.01.1990', 'male')
    person.walk()
    assert person.energy == 90

def test_human_do_homework():
    person = Human('John', 'Doe', '01.01.1990', 'male')
    person.do_homework()
    assert person.energy == 10

if __name__ == '__main__':
    pytest.main()