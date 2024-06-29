from homework_16 import SiteUser
import pytest


@pytest.fixture()
def setup_user():
    return SiteUser(user_name='Serhii', user_email='sobaka@gmail.com', access_level='user')


@pytest.fixture()
def setup_admin():
    return SiteUser(user_name='Ihor', user_email='neSobaka@gmail.com', access_level='admin')


@pytest.fixture()
def setup_another_admin():
    return SiteUser(user_name='Boris', user_email='britva@gmail.com', access_level='admin')


@pytest.fixture()
def setup_moderator():
    return SiteUser(user_name='Kitty', user_email='kitty24@gmail.com', access_level='moderator')


def test_user_initialisation():
    peter = SiteUser(user_name='Peter', user_email='spider@gmail.com', access_level='admin')
    assert peter.user_name == 'Peter'
    assert peter.user_email == 'spider@gmail.com'
    assert peter.access_level == 'admin'
    assert peter.logcount == 0


def test_user_name_change_positive(setup_user):
    assert setup_user.user_name == 'Serhii'
    setup_user.user_name = 'Ihor'
    assert setup_user.user_name == 'Ihor'


def test_user_email_change_positive(setup_user):
    assert setup_user.user_email == 'sobaka@gmail.com'
    setup_user.user_email = 'nesobaka@gmail'
    assert setup_user.user_email == 'nesobaka@gmail'


def test_access_level_change_positive(setup_user):
    assert setup_user.access_level == 'user'
    setup_user.access_level = 'admin'
    assert setup_user.access_level == 'admin'


def test_logcount_change_positive(setup_user):
    assert setup_user.logcount == 0
    setup_user.increment_logcount(3)
    assert setup_user.logcount == 3


def test_user_name_change_negative(setup_user):
    assert setup_user.user_name == 'Serhii'
    with pytest.raises(ValueError, match='Name must be a string'):
        setup_user.user_name = 1


def test_user_email_change_negative(setup_user):
    assert setup_user.user_email == 'sobaka@gmail.com'
    with pytest.raises(ValueError, match='Email must be a string'):
        setup_user.user_email = 1


def test_access_level_change_negative_type(setup_user):
    assert setup_user.access_level == 'user'
    with pytest.raises(ValueError, match='Access must be a string'):
        setup_user.access_level = 1


def test_access_level_change_negative_value(setup_user):
    assert setup_user.access_level == 'user'
    with pytest.raises(ValueError, match='There are only 3 access roles in a system: admin/moderator/user'):
        setup_user.access_level = 'superAdmin'


def test_information_about_user(setup_user):
    expected_str = 'Користувач: Serhii, Електронна пошта: sobaka@gmail.com, Рівень доступу: user'
    assert str(setup_user) == expected_str


def test_users_are_equal(setup_admin, setup_another_admin):
    assert setup_admin == setup_another_admin


def test_users_are_not_equal(setup_admin, setup_moderator):
    assert setup_admin != setup_moderator


if __name__ == '__main__':
    pytest.main()
