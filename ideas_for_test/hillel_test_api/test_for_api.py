import requests
import unittest
import uuid

from hillel_api import API

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

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.email = f"testuser-{uuid.uuid4()}@example.com"
        self.password = "Qwerty12345"
        self.user_data = {
            "name": "John",
            "lastName": "Doe",
            "email": self.email,
            "password": self.password,
            "repeatPassword": self.password
        }

    def tearDown(self):
        self.session.close()

    def test_signup(self):
        response = API.auth.signup(self.session, self.user_data)
        self.assertEqual(response.status_code, 201, "Wrong status code")
        self.assertEqual(response.json()["status"], "ok", "Key 'status' is not ok")

    def test_create_car(self):
        # Sign up and sign in
        API.auth.signup(self.session, self.user_data)
        signin_data = {"email": self.email, "password": self.password, "remember": False}
        API.auth.signin(self.session, signin_data)

        # Create car
        car_data = {"carBrandId": 1, "carModelId": 1, "mileage": 122}
        response = API.cars.cars_post(self.session, car_data)
        self.assertEqual(response.status_code, 201, "Wrong status code")
        self.assertEqual(response.json()["status"], "ok", "Key 'status' is not ok")
        self.car_id = response.json()["data"]["id"]

    def test_update_car(self):
        self.test_create_car()

        # Update car
        update_data = {"id": self.car_id, "carBrandId": 1, "carModelId": 1, "mileage": 500}
        response = API.cars.cars_id_put(self.session, update_data)
        self.assertEqual(response.status_code, 200, "Wrong status code")
        self.assertEqual(response.json()["status"], "ok", "Key 'status' is not ok")
        self.assertEqual(response.json()["data"]["mileage"], 500, "Mileage did not update")

    def test_get_car(self):
        self.test_create_car()

        # Get car data
        response = API.cars.cars_id_get(self.session, {"id": self.car_id})
        self.assertEqual(response.status_code, 200, "Wrong status code")
        self.assertEqual(response.json()["status"], "ok", "Key 'status' is not ok")
        self.assertEqual(response.json()["data"]["id"], self.car_id, "Wrong car id")

    def test_delete_user(self):
        # Sign up and sign in
        API.auth.signup(self.session, self.user_data)
        signin_data = {"email": self.email, "password": self.password, "remember": False}
        API.auth.signin(self.session, signin_data)

        # Delete user
        response = API.users.users(self.session)
        self.assertEqual(response.status_code, 200, "Wrong status code")
        self.assertEqual(response.json()["status"], "ok", "Key 'status' is not ok")

        # Verify user cannot sign in
        response = API.auth.signin(self.session, signin_data)
        self.assertEqual(response.status_code, 400, "Wrong status code")
        self.assertEqual(response.json()["status"], "error", "Key 'status' is not error")

if __name__ == '__main__':
    unittest.main()