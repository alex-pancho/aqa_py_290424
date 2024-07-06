import pytest
from homework_17 import TeamLead, Manager, Developer


# Получаем список атрибутов класса TeamLead
@pytest.fixture()
def team_lead_attributes():
    # ['department', 'name', 'programming_language', 'salary', 'team_size']
    return [attr for attr in dir(TeamLead) if not callable(getattr(TeamLead, attr)) and not attr.startswith('__')]


# Получаем список атрибутов класса Manager
@pytest.fixture()
def manager_attributes():
    # ['department', 'name', 'salary']
    return [attr for attr in dir(Manager) if not callable(getattr(Manager, attr)) and not attr.startswith('__')]


# Получаем список атрибутов класса Developer
@pytest.fixture()
def developer_attributes():
    # ['name', 'programming_language', 'salary']
    return [attr for attr in dir(Developer) if not callable(getattr(Developer, attr)) and not attr.startswith('__')]


# Проверим, что атрибуты класса Manager есть в классе TeamLead
def test_team_lead_inherits_manager_attributes(team_lead_attributes, manager_attributes):
    assert all(attr in team_lead_attributes for attr in manager_attributes)


# Проверим, что атрибуты класса Developer есть в классе TeamLead
def test_team_lead_inherits_developer_attributes(team_lead_attributes, developer_attributes):
    assert all(attr in team_lead_attributes for attr in developer_attributes)


if __name__ == '__main__':
    pytest.main()
