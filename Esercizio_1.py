class Persona:
    def __init__(self,nome,cognome,età):
        self.nome=nome
        self.cognome=cognome
        self.età=età

    def info(self):
        print("Nome: ",self.nome,"-- Cognome: ",self.cognome,"-- Età: ",self.età)

Prova=Persona("Marco","Tripodi","22")
Prova.info()
