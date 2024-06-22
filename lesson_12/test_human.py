import pytest
from lesson_12.homework_12 import Human


# Фикстура, создаёт и возвращает экземпляр класса Human с начальными параметрами для всех тестов
@pytest.fixture()
def setup_person():
    return Human(first_name='Alex', second_name='Shevchenko', birthday='10.07.1986', sex='male')


def test_to_eat(setup_person):
    assert setup_person.energy == 100
    setup_person.to_eat()
    assert setup_person.energy == 105


if __name__ == '__main__':
    pytest.main()
