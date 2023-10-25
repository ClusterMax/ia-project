from src.Modelo import Arbol as Arb
import pytest

#self, padre=None, coordenadas=[], valorReal=None, ValorAcumulado=None, valorHijoMenorAcumulado=None, hijoUp=None, hijoRight=None, hijoBottom=None, hijoLeft=None, tipo="vacio"

#Arbol de ejemplo 1
arbolEjemplo1 = Arb.Arbol()
hijoArriba = Arb.Arbol(arbolEjemplo1, [0,2], 1, 1, None, None, None, None, None, "vacio")
hijoDerecha = Arb.Arbol(arbolEjemplo1, [1,3], 2, 2, None, None, None, None, None, "vacio")
hijoAbajo = Arb.Arbol(arbolEjemplo1, [2,2], 1, 1, None, None, None, None, None, "vacio")
hijoIzquierda = Arb.Arbol(arbolEjemplo1, [1,1], 3, 3, None, None, None, None, None, "vacio")


arbolEjemplo1.set_coordenadas([1,2])
arbolEjemplo1.set_valorReal(0)
arbolEjemplo1.set_hijoUp(hijoArriba)
arbolEjemplo1.set_hijoRight(hijoDerecha)
arbolEjemplo1.set_hijoBottom(hijoAbajo)
arbolEjemplo1.set_hijoLeft(hijoIzquierda)

#Arbol de ejemplo 2
arbolEjemplo2 = Arb.Arbol()
hijoArriba1 = Arb.Arbol(arbolEjemplo1, [1,3], 2, 2, None, None, None, None, None, "vacio")
hijoAbajo1 = Arb.Arbol(arbolEjemplo1, [3,3], 2, 2, None, None, None, None, None, "vacio")
hijoIzquierda1 = Arb.Arbol(arbolEjemplo1, [2,2], 2, 2, None, None, None, None, None, "vacio")


arbolEjemplo2.set_coordenadas([1,2])
arbolEjemplo2.set_valorReal(0)
arbolEjemplo2.set_hijoUp(hijoArriba1)
arbolEjemplo2.set_hijoBottom(hijoAbajo1)
arbolEjemplo2.set_hijoLeft(hijoIzquierda1)




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


@pytest.mark.parametrize(
    "arbol1, arbol2, expected",
    [
        (arbolEjemplo1, arbolEjemplo2, False),
        (arbolEjemplo1,arbolEjemplo1, True),
         (arbolEjemplo2,arbolEjemplo2, True)
    ]
)
def test__eq__(arbol1, arbol2, expected):
    assert arbol1 == arbol2


@pytest.mark.parametrize(
    "",
    [
    ]
)
def test__gt__():
    pass


@pytest.mark.parametrize(
    "",
    [
    ]
)
def test__ge__():
    pass


@pytest.mark.parametrize(
    "",
    [
    ]
)
def test__lt__():
    pass


@pytest.mark.parametrize(
    "",
    [
    ]
)
def test__le__():
    pass
