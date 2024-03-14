from source.contract import Sales 
from datetime import datetime
import pytest
from pydantic import ValidationError

def test_sales_valid_data():

    valid_data = {
        "email": "comprador@example.com",
        "date": datetime.now(),
        "value": 100.50,
        "product": "Product X",
        "amount": 3,
        "category": "category3"
    }

    sales = Sales(**valid_data)

    assert sales.email == valid_data["email"]
    assert sales.date == valid_data["date"]
    assert sales.value == valid_data["value"]
    assert sales.product == valid_data["product"]
    assert sales.amount == valid_data["amount"]
    assert sales.category == valid_data["category"]

def test_sales_invalid_data():

    dados_invalidos = {
        "email": "comprador",
        "data": "not a date",
        "value": -100,
        "product": "",
        "amount": -1,
        "category": 45.2
    }

    with pytest.raises(ValidationError):
        Sales(**dados_invalidos)

def test_category_validation():

    dados = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "value": 100.50,
        "product": "Product Y",
        "amount": 1,
        "category": 45
    }

    with pytest.raises(ValidationError):
        Sales(**dados)

def test_adicional_column():

    dados = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "value": 100.50,
        "product": "product Y",
        "amount": 1,
        "test": "",
        "category": "category3"
    }

    with pytest.raises(ValidationError):
        Sales(**dados)