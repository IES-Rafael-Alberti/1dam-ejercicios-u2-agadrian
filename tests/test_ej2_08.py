import pytest

from src.ej2_08 import nivelRendimiento



@pytest.mark.parametrize(
    "puntuacion,expected",
    [
        (0.0,"Inaceptable"),
        (0.4,"Aceptable"),
        (0.95,"Meritorio"),
        (0.1,"Error"),
        (2,"Meritorio"),
        (-0.5,"Error")

       
    ]
)
def test_nivelRendimiento(puntuacion,expected):
    assert nivelRendimiento(puntuacion) == expected