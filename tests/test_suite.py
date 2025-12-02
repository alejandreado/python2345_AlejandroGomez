import unittest
import sys
sys.path.append('..')

from src.funcion.funciones import esBinario, estaEnRango, estaEnLista

class TestEsBinarioRobusto(unittest.TestCase):
    def testEsBinarioBasicoValido(self):
        self.assertTrue(esBinario("1001"))
        self.assertTrue(esBinario("0"))
        self.assertTrue(esBinario("1"))

    def testEsBinarioBasicoInvalido(self):
        self.assertFalse(esBinario("1021"))
        self.assertFalse(esBinario("prueba"))
        self.assertFalse(esBinario("10 01"))
        self.assertFalse(esBinario(""))

    def testEsBinarioEspaciosYSignos(self):
        self.assertFalse(esBinario(" 1010"))
        self.assertFalse(esBinario("+1010"))
        self.assertFalse(esBinario("-1010"))

    def testEsBinarioCaracteresInvalidos(self):
        self.assertFalse(esBinario("10#1"))
        self.assertFalse(esBinario("10.1"))

    def testEsBinarioTiposInvalidos(self):
        # No acepta tipos no string
        with self.assertRaises(TypeError):
            esBinario(None)
        with self.assertRaises(TypeError):
            esBinario(1010)

    def testEsBinarioGranLongitud(self):
        large = '0' * 10000
        self.assertTrue(esBinario(large))


class TestEstaEnRangoRobusto(unittest.TestCase):
    def testEnRangoInclusivo(self):
        self.assertTrue(estaEnRango(1, 1, 10))
        self.assertTrue(estaEnRango(10, 1, 10))
        self.assertTrue(estaEnRango(5, 1, 10))

    def testFueraDeRango(self):
        self.assertFalse(estaEnRango(0, 1, 10))
        self.assertFalse(estaEnRango(11, 1, 10))

    def testMinMayorMax(self):
        self.assertFalse(estaEnRango(5, 10, 1))

    def testTiposMixtos(self):
        # floats con enteros funcionan
        self.assertTrue(estaEnRango(5.5, 1, 10))
        # strings u None deben provocar TypeError en las comparaciones
        with self.assertRaises(TypeError):
            estaEnRango("5", 1, 10)
        with self.assertRaises(TypeError):
            estaEnRango(5, "1", 10)


class TestEstaEnListaRobusto(unittest.TestCase):
    def setUp(self):
        self.lista = [6, 14, 11, 3, 2, 1, 15, 19]

    def testElementoPresente(self):
        for v in [6, 11, 19, 1]:
            self.assertTrue(estaEnLista(v, self.lista))

    def testElementoNoPresente(self):
        for v in [5, 10, 100]:
            self.assertFalse(estaEnLista(v, self.lista))

    def testListaVacia(self):
        self.assertFalse(estaEnLista(1, []))

    def testTiposEnLista(self):
        mixed = ["1", 1, None, (1,)]
        self.assertTrue(estaEnLista(1, mixed))
        self.assertTrue(estaEnLista("1", mixed))
        self.assertFalse(estaEnLista(2, mixed))

    def testListaNoIterable(self):
        with self.assertRaises(TypeError):
            estaEnLista(1, None)

    def testListaConDuplicados(self):
        lst = [1, 2, 2, 3]
        self.assertTrue(estaEnLista(2, lst))


if __name__ == '__main__':
    unittest.main()
