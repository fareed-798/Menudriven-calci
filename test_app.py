import pytest
from app import add, subtract, app
def test_add():
    assert add(10,5)==15
    assert add(-1, 1)==0
def test_subtract():
    assert subtract(10,5)==5
    assert subtract(0,5)==-5
def test_api_add():
    client = app.test_client()
    response = client.post('/calculate',json={'operation':'add','a':10,'b':5})
    assert response.status_code==200
    assert response.get_json()['result']==15