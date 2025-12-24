import currency_converter

class DevisesLogic:
    def __init__(self):
        self.c = currency_converter.CurrencyConverter()

    def convertir(self, montant, de_devise, vers_devise):
        if montant < 0:
            raise ValueError("Le montant ne peut pas être négatif")
        return self.c.convert(montant, de_devise, vers_devise)

