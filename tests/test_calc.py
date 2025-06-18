
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to Python path

from calc import app



import pytest
from calc import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if homepage loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Simple Calculator" in response.data

def test_addition(client):
    """Test addition operation"""
    response = client.get('/result?num1=5&num2=3&operation=add')
    assert response.status_code == 200
    assert b"Result: 8.0" in response.data

def test_subtraction(client):
    """Test subtraction operation"""
    response = client.get('/result?num1=10&num2=4&operation=subtract')
    assert response.status_code == 200
    assert b"Result: 6.0" in response.data

def test_multiplication(client):
    """Test multiplication operation"""
    response = client.get('/result?num1=6&num2=7&operation=multiply')
    assert response.status_code == 200
    assert b"Result: 42.0" in response.data

def test_division(client):
    """Test division operation"""
    response = client.get('/result?num1=8&num2=2&operation=divide')
    assert response.status_code == 200
    assert b"Result: 4.0" in response.data

def test_division_by_zero(client):
    """Test division by zero error handling"""
    response = client.get('/result?num1=8&num2=0&operation=divide')
    assert response.status_code == 200
    assert b"Error: Division by zero" in response.data
