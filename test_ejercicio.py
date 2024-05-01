import unittest
import ejercicio

class TestFrutasLocas(unittest.TestCase):
    def test_frutas(self):
        frutas = ejercicio.frutas
        self.assertEqual(frutas["manzana"], "roja")
        self.assertEqual(frutas["banana"], "amarilla")
        self.assertEqual(frutas["pera"], "verde")
        self.assertEqual(frutas["naranja"], "naranja")
        self.assertEqual(frutas.get("uva"), None)
