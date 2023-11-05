import pytest

from src.ej2_07 import tipoImpositivo



@pytest.mark.parametrize(
    "rentaAnual,expected",
    [
        (666,5),
        (0,5),
        (1,5),
        (15000,15),
        (20000,20),
        (120000,45),
        (1562.23,5) 
    ]
)
def test_tipoImpositivo(rentaAnual,expected):
    assert tipoImpositivo(rentaAnual) == expected