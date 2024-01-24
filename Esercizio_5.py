class Prodotto:
    def __init__(self,nome,prezzo,quantità_disponibile):
        self.nome=nome
        self.prezzo=prezzo
        self.qta=quantità_disponibile
    def product(self):
        if self.qta==0:
            print("Prodotto non disponibile!")
        elif self.prezzo<=0:
            print("Prezzo inserito non valido!")
        else:
            costo=self.prezzo*self.qta
            print(costo)
            return costo

elemento1=Prodotto("Bicicletta",259.99,2)

elemento1.product()