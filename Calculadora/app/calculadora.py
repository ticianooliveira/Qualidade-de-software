import unittest

# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n - 1)
    
def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    if not isinstance(n, int):
        raise TypeError("Fatorial só é definido para números inteiros")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

class TestFatorial(unittest.TestCase):
    def test_fatorial_positivo(self):
        self.assertEqual(fatorial(5), 120)

    def test_fatorial_zero(self):
        self.assertEqual(fatorial(0), -1)

    def test_fatorial_maior_que_zero(self):
        self.assertTrue(fatorial(5) > 0)  

    def test_fatorial_nao_negativo(self):
        self.assertFalse(fatorial(5) < 0) 

    # ... outros casos de teste

if __name__ == '__main__':
    print("Chamando o unittest.main!")
    unittest.main()