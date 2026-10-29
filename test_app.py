import pytest
from app import add, subtract, multiply, divide, app
def test_add():
    assert add(10, 5) == 15
def test_subtract():
    assert subtract(10, 5) == 5
def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-2, 4) == -8
def test_divide():
    assert divide(10, 2) == 5.0
    with pytest.raises(ValueError):
        divide(5, 0)
def test_api_multiply_and_divide():
    client = app.test_client()
    res_mul = client.post('/calculate', json={'operation': 'multiply', 'a': 4, 'b': 5})
    assert res_mul.get_json()['result'] == 20
    res_div = client.post('/calculate', json={'operation': 'divide', 'a': 10, 'b': 2})
    assert res_div.get_json()['result'] == 5.0