import pytest
from src.ej2_05 import comprobarTributacion


@pytest.mark.parametrize(
    "edad,ingreso,expected",
    [
        (17,1200,True),
        (16,1200,False),
        (18,999,False),
        (20,1001,True)
        
        
    ]
)
def test_comprobarTributacion(edad, ingreso, expected):
    assert comprobarTributacion(edad, ingreso) == expected