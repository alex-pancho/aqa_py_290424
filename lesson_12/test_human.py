import pytest
from homework_12 import Human  

@pytest.fixture
def human_1():
    return Human("Vasyl", "Vasylenko", "11/01/91", "male")

@pytest.fixture
def human_2():
    return Human("Gavryk", "Gavrychenko", "12/02/92", "male")

@pytest.fixture
def human_3():
    return Human("Mykola", "Mykolenko", "13/03/93", "male")

@pytest.fixture
def human_4():
    return Human("Galyna", "Galychenko", "14/04/94", "female")

@pytest.fixture
def human_5():
    return Human("Daryna", "Darychenko", "15/05/95", "female")

def test_initialization(human_1):
    assert human_1.first_name == "Vasyl"
    assert human_1.last_name == "Vasylenko"
    assert human_1.birth_date == "11/01/91"
    assert human_1.gender == "male"
    assert human_1.energy == 100

def test_eat(human_1):
    human_1.eat()
    assert human_1.energy == 105

def test_sleep(human_1):
    human_1.sleep()
    assert human_1.energy == 110

def test_talk(human_1):
    human_1.talk()
    assert human_1.energy == 95

def test_walk(human_1):
    human_1.walk()
    assert human_1.energy == 90

def test_do_homework(human_1):
    human_1.do_homework()
    assert human_1.energy == 10

def test_combined_actions(human_1):
    human_1.eat()
    human_1.sleep()
    human_1.walk()
    assert human_1.energy == 105

   