from src.Modelo import CostoUniformeRecursivo
import pytest


@pytest.mark.parametrize(
    "respuestaAlgoritmo, respuestaEsperada",
    [
        (5, 5),
        (4, 4),
        (4, 4),
        (3, 3)
    ]
)
def test_CostoUniformeRecursivo_params(respuestaAlgoritmo, respuestaEsperada):
    assert respuestaAlgoritmo == respuestaEsperada