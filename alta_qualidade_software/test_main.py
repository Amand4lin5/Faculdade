from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_conversion_accuracy():
    # Testar conversão de USD para EUR
    response = client.post(
        "/convert/",
        data={"from_currency": "USD", "to_currency": "EUR", "amount": 100}
    )
    assert response.status_code == 200
    assert response.json()["converted_amount"] == 85.0  # Exemplo de valor esperado

def test_invalid_currency():
    # Testar se a API responde corretamente a uma moeda inválida
    response = client.post(
        "/convert/",
        data={"from_currency": "INVALID", "to_currency": "EUR", "amount": 100}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Moeda INVALID não suportada."}

def test_negative_amount():
    # Testar conversão com um valor negativo (cenário negativo)
    response = client.post(
        "/convert/",
        data={"from_currency": "USD", "to_currency": "EUR", "amount": -50}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Quantidade inválida"}

def test_zero_amount():
    # Testar conversão com valor zero
    response = client.post(
        "/convert/",
        data={"from_currency": "USD", "to_currency": "EUR", "amount": 0}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Quantidade inválida"}
