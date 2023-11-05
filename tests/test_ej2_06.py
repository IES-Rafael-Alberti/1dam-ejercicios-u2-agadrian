import pytest

from src.ej2_06 import grupoCorrespondiente



@pytest.mark.parametrize(
    "nombre,sexo,expected",
    [
        ("Mario","masculino","B"),
        ("Maria","femenino","B"),
        ("oliver","masculino","A"),
        ("adriana","femenino","A")
    ]
)
def test_grupoCorrespondiente(nombre, sexo, expected):
    assert grupoCorrespondiente(nombre, sexo) == expected