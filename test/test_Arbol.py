from src.Modelo import Arbol
import pytest


@pytest.mark.parametrize(
    "arbolTest, expected",
    [
        (5, 5),
        (4, 4),
        (4, 4),
        (3, 3)
    ]
)
def test_Arbol_params(arbolTest, expected):
    assert arbolTest == expected