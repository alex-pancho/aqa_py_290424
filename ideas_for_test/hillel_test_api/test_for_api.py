from hillel_api import API
import requests

s = requests.session()


def test_signup_positive():

    user_data = {
        "name": "John",
        "lastName": "Dou",
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "repeatPassword": "Qam2608venv"
    }
    r = API.auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json['data']['currency'] in ['eur', 'gbp', 'usd', 'uah', 'pln'], 'Wrong currency'
    assert r_json['data']['distanceUnits'] == 'km', 'Wrong distanceUnits'
    assert isinstance(r_json['data']['userId'], int), 'userId is not an integer'


def test_signin_positive():

    user_data = {
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    r = API.auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json['data']['currency'] in ['eur', 'gbp', 'usd', 'uah', 'pln'], 'Wrong currency'
    assert r_json['data']['distanceUnits'] == 'km', 'Wrong distanceUnits'
    assert isinstance(r_json['data']['userId'], int), 'userId is not an integer'


def test_signin_negative():

    user_data_negative = {
        "email": "qam@2022test.com",
        "password": "Qam2",
        "remember": False
    }
    r = API.auth.signin(s, user_data_negative)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"
    assert r_json['message'] == 'Wrong email or password', 'Wrong message'


def test_logout():

    r = API.auth.logout(s)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_signin_delete_and_cant_resign():
    """E2E test example"""
    user_data = {
        "email": "qam0404@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    r = API.auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json['data']['currency'] in ['eur', 'gbp', 'usd', 'uah', 'pln'], 'Wrong currency'
    assert r_json['data']['distanceUnits'] == 'km', 'Wrong distanceUnits'
    assert isinstance(r_json['data']['userId'], int), 'userId is not an integer'
    # delte user
    r = API.users.users(s)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    # cant login
    r = API.auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'error' expected"
    assert r_json['message'] == 'Wrong email or password', 'Wrong message'
