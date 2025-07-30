from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_listar_cifra():
    # Criar nova cifra
    response = client.post("/cifras/", json={
        "nome": "Test Song",
        "banda": "Test Band",
        "nivel": "iniciante",
        "pestana": False,
        "capotraste": False,
        "tonalidade": "C",
        "genero": "Pop",
        "dedilhado": True,
        "levada": False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Test Song"
    assert data["banda"] == "Test Band"

    # Listar cifras
    response = client.get("/cifras/")
    assert response.status_code == 200
    lista = response.json()
    assert any(cifra["nome"] == "Test Song" for cifra in lista)