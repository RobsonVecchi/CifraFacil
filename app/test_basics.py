import pytest
from .validators import validar_nivel
from fastapi import HTTPException

def test_iniciante_com_pestana():
    with pytest.raises(HTTPException) as exc_info:
        validar_nivel("iniciante", True)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Nível iniciante não pode ter pestana."

def test_iniciante_sem_pestana():
    # Não deve lançar exceção
    validar_nivel("iniciante", False)

def test_intermediaria_com_pestana():
    validar_nivel("intermediária", True)

def test_intermediaria_sem_pestana():
    validar_nivel("intermediária", False)