import requests


def test_get_response_check_status_code_200():
    response = requests.get("https://api.github.com/events")
    assert response.status_code == 200


def test_get_response_check_type():
    response = requests.get("https://api.github.com/users/test987987")
    response_body = response.json()
    assert response_body["type"] == "User"


def test_get_response_check_headers():
    response = requests.get("https://api.github.com/events")
    response_body = response.headers
    assert response_body["Content-Type"] == "application/json; charset=utf-8"
