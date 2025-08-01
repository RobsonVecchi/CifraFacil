from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_listar_cifra():
    # Criar nova cifra válida
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

def test_criar_cifra_invalida():
    # Deve falhar ao criar cifra com nível iniciante e pestana True
    response = client.post("/cifras/", json={
        "nome": "Test Fail",
        "banda": "Fail Band",
        "nivel": "iniciante",
        "pestana": True,
        "capotraste": False,
        "tonalidade": "C",
        "genero": "Pop",
        "dedilhado": True,
        "levada": False
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Nível iniciante não pode ter pestana."