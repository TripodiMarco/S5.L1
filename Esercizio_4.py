class Conto:
    def __init__(self,saldo):
        self.saldo=saldo
    def deposito(self, ammontare):
        self.saldo+=ammontare
    def prelievo(self, prelievo):
        if self.saldo>=prelievo:
            self.saldo-=prelievo
        else:
            print("La cifra richiesta è superiore al saldo disponibile!")
    def saldo_contabile(self):
        print("Il saldo contabile è pari a:",self.saldo)

saldo_finale=Conto(1546)


saldo_finale.deposito(0)
saldo_finale.prelievo(1559)
saldo_finale.saldo_contabile()
