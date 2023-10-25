import pytest
from EjerciciosU2.ej2_01 import pedirEdad, mayorEdad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, False),
        (18, True),
        (100, True),
        (5, False),
        (17, False),
        (125, True)
    ]
)
def test_mayorEdad_params(input_n, expected):
    assert mayorEdad(input_n) == expected


"""
Este tipo de test no tenéis que hacerlos, pero para que veáis cómo se haría con un mock...

Un mock es un objeto dummy, un objeto falso que devuelve lo que nosotros queremos o necesitamos para usar dentro del test.
"""

def test_pedirEdad(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "15")
    result = pedirEdad()
    assert result == 15
    monkeypatch.setattr('builtins.input', lambda _: "1")
    result = pedirEdad()
    assert result == 1
    monkeypatch.setattr('builtins.input', lambda _: "100")
    result = pedirEdad()
    assert result == 100
