import pytest
from src.ej2_02 import pedirContraseña

@pytest.mark.parametrize(
    "expected",
    [
        ("123")
        
    ]
)
def test_pedir_contraseña(expected):
    assert pedirContraseña() == expected