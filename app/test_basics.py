from validators import validar_nivel

def test_iniciante_com_pestana():
    assert validar_nivel(True, "iniciante") == False

def test_iniciante_sem_pestana():
    assert validar_nivel(False, "iniciante") == True

def test_intermediaria_com_pestana():
    assert validar_nivel(True, "intermediária") == True

def test_intermediaria_sem_pestana():
    assert validar_nivel(False, "intermediária") == True