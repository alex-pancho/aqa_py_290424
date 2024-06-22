import pytest
from homework_12 import Human


# Фикстура, создаёт и возвращает экземпляр класса Human с начальными параметрами для всех тестов
@pytest.fixture()
def setup_person():
    return Human(first_name='Alex', second_name='Shevchenko', birthday='10.07.1986', sex='male')


def test_human_initialization():
    human = Human(first_name='Oleg', second_name='Panasenko', birthday='06.11.1989', sex='male')
    assert human.first_name == 'Oleg'
    assert human.second_name == 'Panasenko'
    assert human.birthday == '06.11.1989'
    assert human.sex == 'male'
    assert human.energy == 100


def test_human_attribute_name_change(setup_person):
    assert setup_person.first_name == 'Alex'
    setup_person.first_name = 'Serhii'
    assert setup_person.first_name == 'Serhii'


def test_human_attribute_second_name_change(setup_person):
    assert setup_person.second_name == 'Shevchenko'
    setup_person.second_name = 'Makarenko'
    assert setup_person.second_name == 'Makarenko'


def test_human_attribute_sex_change(setup_person):
    assert setup_person.sex == 'male'
    setup_person.sex = 'female'
    assert setup_person.sex == 'female'


def test_human_attribute_types(setup_person):
    assert isinstance(setup_person.first_name, str)
    assert isinstance(setup_person.second_name, str)
    assert isinstance(setup_person.birthday, str)
    assert isinstance(setup_person.sex, str)
    assert isinstance(setup_person.energy, int)


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
