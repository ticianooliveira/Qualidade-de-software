import unittest
import pytest

from app.calculadora import fatorial


# class TestFatorial(unittest.TestCase):
#     def test_fatorial_positivo(self):
#         self.assertEqual(fatorial(5), 120)

#     def test_fatorial_zero(self):
#         self.assertEqual(fatorial(0), 1)

#     def test_fatorial_maior_que_zero(self):
#         self.assertTrue(fatorial(5) > 0)  

#     def test_fatorial_nao_negativo(self):
#         self.assertFalse(fatorial(5) < 0) 

    # ... outros casos de teste

def test_fatorial_decimal():
        with pytest.raises(TypeError):
            fatorial(3.5)
            fatorial(3.55)
            fatorial(3.555)