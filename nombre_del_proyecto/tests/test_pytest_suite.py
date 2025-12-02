import pytest

from src.funcion.funciones import esBinario, estaEnRango, estaEnLista

# -------- esBinario tests (pytest) --------
@pytest.mark.parametrize("s", ["0", "1", "1010", "111000111"])
def testEsBinarioValido(s):
    assert esBinario(s) is True


@pytest.mark.parametrize("s", ["", "10 01", "1021", "10#1", "10.1", "prueba"]) 
def testEsBinarioInvalido(s):
    assert esBinario(s) is False


def testEsBinarioGranCadena():
    large = '1' * 20000
    assert esBinario(large) is True


def testEsBinarioTiposNoString():
    with pytest.raises(TypeError):
        esBinario(None)
    with pytest.raises(TypeError):
        esBinario(1010)


# -------- estaEnRango tests (pytest) --------
@pytest.mark.parametrize("valor,minimo,maximo,expected", [
    (1, 1, 10, True),
    (10, 1, 10, True),
    (5, 1, 10, True),
    (0, 1, 10, False),
    (11, 1, 10, False),
])
def testEstaEnRangoParam(valor, minimo, maximo, expected):
    assert estaEnRango(valor, minimo, maximo) is expected


def testEstaEnRangoMinMayorMax():
    # Rango inválido: mínimo mayor que máximo — función debe devolver False
    assert estaEnRango(5, 10, 1) is False


def testEstaEnRangoTiposMixtos():
    # float vs int comparables
    assert estaEnRango(5.5, 1, 10) is True
    # strings deben provocar TypeError al comparar
    with pytest.raises(TypeError):
        estaEnRango("5", 1, 10)
    with pytest.raises(TypeError):
        estaEnRango(5, "1", 10)


# -------- estaEnLista tests (pytest) --------
@pytest.fixture
def lista_especial():
    return [6, 14, 11, 3, 2, 1, 15, 19]


@pytest.mark.parametrize("v", [6, 11, 19, 1])
def testEstaEnListaElementosPresentes(v, lista_especial):
    assert estaEnLista(v, lista_especial) is True


@pytest.mark.parametrize("v", [5, 10, 100])
def testEstaEnListaElementosNoPresentes(v, lista_especial):
    assert estaEnLista(v, lista_especial) is False


def testEstaEnListaListaVacia():
    assert estaEnLista(1, []) is False


def testEstaEnListaTiposMezclados():
    mixed = ["1", 1, None, (1,)]
    assert estaEnLista(1, mixed) is True
    assert estaEnLista("1", mixed) is True
    assert estaEnLista(2, mixed) is False


def testEstaEnListaNoIterable():
    with pytest.raises(TypeError):
        estaEnLista(1, None)


def testEstaEnListaDuplicados():
    lst = [1, 2, 2, 3]
    assert estaEnLista(2, lst) is True