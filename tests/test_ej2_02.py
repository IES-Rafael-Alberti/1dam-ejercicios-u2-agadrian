import pytest
from src.ej2_02 import comprobarContraseña

@pytest.mark.parametrize(
    "input_n,input_n2,expected",
    [
        ("p4ssw0rd","p4ssw0rd",True),
        ("pedroklk","PEDROKLK",True),
        ("pedroklk","wermok",False),
        ("123","4546754",False)
        
    ]
)
def test_comprobarContraseña(input_n, input_n2, expected):
    assert comprobarContraseña(input_n, input_n2) == expected