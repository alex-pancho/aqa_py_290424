import requests

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

# XPath locators
xpath_locators = {
    "login_button": "//button[text()='Login']",
    "username_input": "//input[@name='email' and @type='text']",
    "password_input": "//input[@name='password' and @type='password']",
    "submit_login": "//button[@type='submit' and text()='Login']",
    "home_page_title": "//h1[text()='Your Garage']",
    "add_car_button": "//button[@class='btn btn-dark' and contains(text(),'Add car')]",
    "car_brand_dropdown": "//select[@name='carBrand']",
    "car_model_dropdown": "//select[@name='carModel']",
    "car_fuel_type_dropdown": "//select[@name='carFuelType']",
    "car_registration_input": "//input[@name='carRegistration']",
    "add_car_submit_button": "//button[@type='submit' and text()='Add']",
    "garage_title": "//h1[text()='Your Garage']",
    "profile_button": "//a[@href='/profile']",
    "profile_page_title": "//h1[text()='Profile']",
    "first_name_input": "//input[@name='firstName']",
    "last_name_input": "//input[@name='lastName']",
    "update_profile_button": "//button[@type='submit' and text()='Update']",
    "logout_button": "//button[text()='Logout']",
    "register_link": "//a[text()='Register']",
    "register_username_input": "//input[@name='email' and @type='text']",
    "register_password_input": "//input[@name='password' and @type='password']",
    "register_password_confirm_input": "//input[@name='confirmPassword' and @type='password']",
    "submit_register_button": "//button[@type='submit' and text()='Register']",
    "forgot_password_link": "//a[text()='Forgot your password?']",
    "reset_email_input": "//input[@name='email' and @type='text']",
    "reset_password_button": "//button[@type='submit' and text()='Reset password']",
    "car_list": "//div[@class='car_list']",
    "car_list_item": "//div[@class='car_list_item']",
    "car_item_name": "//div[@class='car_list_item']//div[@class='car_list_item__name']",
    "car_item_model": "//div[@class='car_list_item']//div[@class='car_list_item__model']",
    "car_item_fuel": "//div[@class='car_list_item']//div[@class='car_list_item__fuel']",
    "edit_car_button": "//button[@class='btn btn-warning' and text()='Edit']",
    "delete_car_button": "//button[@class='btn btn-danger' and text()='Delete']",
    "confirm_delete_button": "//button[@class='btn btn-danger' and text()='Yes']",
    "cancel_delete_button": "//button[@class='btn btn-secondary' and text()='Cancel']",
    "back_to_garage_button": "//button[@class='btn btn-dark' and text()='Back to Garage']",
    "service_history_button": "//a[text()='Service History']",
    "service_history_title": "//h1[text()='Service History']",
    "add_service_button": "//button[@class='btn btn-dark' and contains(text(),'Add service')]",
    "service_date_input": "//input[@name='serviceDate']",
    "service_description_input": "//input[@name='serviceDescription']",
    "service_cost_input": "//input[@name='serviceCost']",
    "submit_service_button": "//button[@type='submit' and text()='Add service']",
    "service_list": "//div[@class='service_list']",
    "service_item": "//div[@class='service_list_item']",
    "edit_service_button": "//button[@class='btn btn-warning' and text()='Edit service']",
    "delete_service_button": "//button[@class='btn btn-danger' and text()='Delete service']",
    "confirm_service_delete_button": "//button[@class='btn btn-danger' and text()='Yes, delete service']",
    "cancel_service_delete_button": "//button[@class='btn btn-secondary' and text()='Cancel']"
}

