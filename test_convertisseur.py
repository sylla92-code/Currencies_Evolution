import unittest
from calculateur import DevisesLogic

class TestMonConvertisseur(unittest.TestCase):
    def setUp(self):
        """S'exécute avant chaque test"""
        self.logic = DevisesLogic()

    def test_conversion_eur_chf(self):
        """Vérifie que la conversion de 10 EUR donne un résultat cohérent"""
        resultat = self.logic.convertir(10, "EUR", "CHF")
        self.assertGreater(resultat, 0) # Le résultat doit être > 0
        print(f"Test 10 EUR -> CHF : {resultat}")

    def test_montant_negatif(self):
        """Vérifie que le programme refuse les montants négatifs"""
        with self.assertRaises(ValueError):
            self.logic.convertir(-10, "EUR", "CHF")

if __name__ == '__main__':
    unittest.main()