import pytest
from homework_12 import Human


# Фикстура, создаёт и возвращает экземпляр класса Human с начальными параметрами для всех тестов
@pytest.fixture()
def setup_person():
    return Human(first_name='Alex', second_name='Shevchenko', birthday='10.07.1986', sex='male')


def test_to_eat(setup_person):
    assert setup_person.energy == 100
    setup_person.to_eat()
    assert setup_person.energy == 105


def test_to_sleep(setup_person):
    assert setup_person.energy == 100
    setup_person.to_sleep()
    assert setup_person.energy == 110


def test_to_talk(setup_person):
    assert setup_person.energy == 100
    setup_person.to_talk()
    assert setup_person.energy == 95


def test_to_walk(setup_person):
    assert setup_person.energy == 100
    setup_person.to_walk()
    assert setup_person.energy == 90


def test_do_homework(setup_person):
    assert setup_person.energy == 100
    setup_person.to_do_homework()
    assert setup_person.energy == 10


if __name__ == '__main__':
    pytest.main()
