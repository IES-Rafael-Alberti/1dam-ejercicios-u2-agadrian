import pytest
from src.ej2_03 import dividirNumeros

@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (8,2,float(8/2)),
        (6,0,None),
        (44,4,float(44/4))
        
    ]
)
def test_dividirNumeros(num1, num2, expected):
    assert dividirNumeros(num1, num2) == expected