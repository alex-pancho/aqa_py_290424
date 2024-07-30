import pytest
import requests
from hillel_api import API

base_api_url = "https://qauto.forstudy.space/api"

@pytest.fixture(scope="session")
def session():
    return requests.session()

@pytest.fixture(scope="module")
def user_data():
    return {
        "name": "Jhn",
        "lastName": "De",
        "email": "t1estuser@example.com",
        "password": "TestPass123!",
        "repeatPassword": "TestPass123!"
    }

@pytest.fixture(scope="module")
def car_data():
    return {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1000
    }

def test_signup_positive(session, user_data):
    r = API.auth.signup(session, user_data)
    r_json = r.json()
    assert r.status_code == 201, f"Wrong status code: {r.status_code}, {r.text}"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

def test_create_car(session, user_data, car_data):
    signin_data = {
        "email": user_data["email"],
        "password": user_data["password"],
        "remember": False
    }
    signin_response = API.auth.signin(session, signin_data)
    assert signin_response.status_code == 200, f"Signin failed: {signin_response.status_code}, {signin_response.text}"

    r = API.cars.cars_post(session, car_data)
    r_json = r.json()
    assert r.status_code == 201, f"Wrong status code: {r.status_code}, {r.text}"
    assert "id" in r_json, "Car ID not in response"

    car_data["id"] = r_json["id"]  # Save car ID for later tests

def test_edit_car(session, user_data, car_data):
    signin_data = {
        "email": user_data["email"],
        "password": user_data["password"],
        "remember": False
    }
    signin_response = API.auth.signin(session, signin_data)
    assert signin_response.status_code == 200, f"Signin failed: {signin_response.status_code}, {signin_response.text}"

    # Make sure the car exists
    create_response = API.cars.cars_post(session, car_data)
    assert create_response.status_code == 201, f"Car creation failed: {create_response.status_code}, {create_response.text}"
    car_id = create_response.json()["id"]
    car_data["id"] = car_id

    car_data["mileage"] = 2000  # Update mileage
    r = API.cars.cars_id_put(session, car_data)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code: {r.status_code}, {r.text}"
    assert r_json["data"]["mileage"] == 2000, "Mileage not updated"

def test_get_car_data(session, user_data, car_data):
    signin_data = {
        "email": user_data["email"],
        "password": user_data["password"],
        "remember": False
    }
    signin_response = API.auth.signin(session, signin_data)
    assert signin_response.status_code == 200, f"Signin failed: {signin_response.status_code}, {signin_response.text}"

    # Make sure the car exists
    create_response = API.cars.cars_post(session, car_data)
    assert create_response.status_code == 201, f"Car creation failed: {create_response.status_code}, {create_response.text}"
    car_id = create_response.json()["id"]
    car_data["id"] = car_id

    r = API.cars.cars_id_get(session, {"id": car_id})
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code: {r.status_code}, {r.text}"
    assert r_json["data"]["id"] == car_id, "Wrong car ID"

def test_delete_user(session, user_data):
    signin_data = {
        "email": user_data["email"],
        "password": user_data["password"],
        "remember": False
    }
    signin_response = API.auth.signin(session, signin_data)
    assert signin_response.status_code == 200, f"Signin failed: {signin_response.status_code}, {signin_response.text}"

    r = API.users.users(session)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code: {r.status_code}, {r.text}"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
