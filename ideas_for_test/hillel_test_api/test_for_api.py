from hillel_api import API
import requests

s = requests.session()


def test_sigup_positive():

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


def test_sigin_positive():

    user_data = {
    "email": "qam0404@2022test.com",
    "password": "Qam2608venv",
    "remember": False
    }
    r = API.auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_sigin_negative():

    user_data_negative = {
    "email": "qam@2022test.com",
    "password": "Qam2",
    "remember": False
    }
    r = API.auth.signin(s, user_data_negative)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_logout():

    r = API.auth.logout(s)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_sigin_delete_and_cant_resign():
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

    
    
def test_resset_password_positive():
    user_data = {
        "user_id": 133645, #valid user id
        "token": "valid_token" #valid token
        }
    r = API.users.resetpassword(s, user_data)
    r_json = r.json()
    assert r.status_code == 200,"Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_resset_password_negative_invalid_user_id():
    user_data = {
        "user_id": 999999, #invalid user id
        "token": "valid_token"  #valid token
    }
    r = API.users.resetpassword(s, user_data)
    r_json = r.json()
    assert r.status_code == 404,"Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_resset_password_negative_invalid_token():
    user_data = {
        "user_id": 133645, #valid user id
        "token": "invalid_token"  #invalid token
    }
    r = API.users.resetpassword(s, user_data)
    r_json = r.json()
    assert r.status_code == 404,"Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_resset_password_negative_no_user_id():
    user_data = {
        "token": "ivalid_token"  #ivalid token
    }
    r = API.users.resetpassword(s, user_data)
    r_json = r.json()
    assert r.status_code == 404,"Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"     


def test_resset_password_negative_no_token():
    user_data = {
        "user_id": 133645, #valid user id
    }
    r = API.users.resetpassword(s, user_data)
    r_json = r.json()
    assert r.status_code == 404,"Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_resset_password_negative_empty_request():
    user_data = {}
    r = API.users.resetpassword(s, user_data)
    r_json = r.json()
    assert r.status_code == 404,"Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"
