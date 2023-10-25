import pytest
from src.ej2_02 import pedirContraseña

@pytest.mark.parametrize(
    "expected",
    [
        (123)
        
    ]
)
def test_mayorEdad_params(expected):
    assert pedirContraseña() == expected