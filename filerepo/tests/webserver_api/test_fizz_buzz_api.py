from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
client = TestClient(app)

def test_one_returns_one_as_string():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_one_returns_one_as_string():
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"output" : "1"}


def test_int_returns_int_as_string():
    response = client.get("/2")
    assert response.status_code == 200
    assert response.json() == {"output" : "2"}


def test_three_returns_fizz():
    response = client.get("/3")
    assert response.status_code == 200
    assert response.json() == {"output" : "Fizz"}


def test_div_by_three_returns_Fizz():
    response = client.get("/18")
    assert response.status_code == 200
    assert response.json() == {"output" : "Fizz"}


def test_five_returns_Buzz():
    response = client.get("/5")
    assert response.status_code == 200
    assert response.json() == {"output" : "Buzz"}


def test_div_by_five_returns_Buzz():
    response = client.get("/25")
    assert response.status_code == 200
    assert response.json() == {"output" : "Buzz"}


def test_div_by_both_returns_fizzbuzz():
    response = client.get("/30")
    assert response.status_code == 200
    assert response.json() == {"output" : "FizzBuzz"}

