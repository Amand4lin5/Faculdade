import unittest
import numpy as np
from src.Calculadora import fatorial, logaritmo_natural, logaritmo_base10, cosseno, seno, tangente, adicao
import unittest

class TestCalculadora(unittest.TestCase):


    def test_adicao(self):
        self.assertEqual(adicao(3, 4), 7)# Testa a soma de números positivos
        self.assertEqual(adicao(-3, -4), -7)# Testa a soma de números negativos
        self.assertEqual(adicao(5, -3), 2) # Testa a soma de número positivo e negativo
        self.assertEqual(adicao(0, 0), 0)# Testa a soma com zero
        self.assertEqual(adicao(5, 0), 5)

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)  # Fatorial de 0 é 1
        self.assertEqual(fatorial(1), 1)  # Fatorial de 1 é 1
        self.assertEqual(fatorial(5), 120)  # Fatorial de 5 é 120
        self.assertEqual(fatorial(10), 3628800)  # Fatorial de 10 é 3628800

    def test_logaritmo_natural(self):
        self.assertEqual(logaritmo_natural(-1), "Erro: Logaritmo de número não positivo")  # Teste com número negativo
        self.assertEqual(logaritmo_natural(0), "Erro: Logaritmo de número não positivo")  # Teste com zero
        self.assertAlmostEqual(logaritmo_natural(1), 0.0)  # ln(1) = 0
        self.assertAlmostEqual(logaritmo_natural(np.e), 1.0)  # ln(e) = 1
        self.assertAlmostEqual(logaritmo_natural(10), np.log(10))  # Comparação com valor calculado pelo NumPy
        
    def test_logaritmo_base10(self):
        self.assertEqual(logaritmo_base10(-1), "Erro: Logaritmo de número não positivo")  # Número negativo
        self.assertEqual(logaritmo_base10(0), "Erro: Logaritmo de número não positivo")   # Zero
        self.assertAlmostEqual(logaritmo_base10(1), 0.0)  # log10(1) = 0
        self.assertAlmostEqual(logaritmo_base10(10), 1.0)  # log10(10) = 1
        self.assertAlmostEqual(logaritmo_base10(100), 2.0)  # log10(100) = 2

    def test_seno(self):
        self.assertAlmostEqual(seno(0, radianos=False), 0.0)
        self.assertAlmostEqual(seno(90, radianos=False), 1.0)
        self.assertAlmostEqual(seno(30, radianos=False), 0.5)

    def test_cosseno(self):
        self.assertAlmostEqual(cosseno(0, radianos=False), 1.0)
        self.assertAlmostEqual(cosseno(90, radianos=False), 0.0)
        self.assertAlmostEqual(cosseno(60, radianos=False), 0.5)

    def test_tangente(self):
        self.assertAlmostEqual(tangente(0, radianos=False), 0.0)
        self.assertAlmostEqual(tangente(45, radianos=False), 1.0)
        self.assertEqual(tangente(90, radianos=False), "Erro: Tangente indefinida para este ângulo")
        self.assertEqual(tangente(270, radianos=False), "Erro: Tangente indefinida para este ângulo")

