import pytest

from src.ej2_09 import precioAcceso



@pytest.mark.parametrize(
    "edad,expected",
    [
        (0,0),
        (2,0),
        (4,5),
        (6,5),
        (10,5),
        (15,5),
        (18,5),
        (20,10),
        (86,10)
    ]
)
def test_precioAcceso(edad,expected):
    assert precioAcceso(edad) == expected