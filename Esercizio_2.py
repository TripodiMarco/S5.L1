class Libro:
    def __init__(self,titolo,autore,anno_di_pubblicazione):
        self.nome=titolo
        self.autore=autore
        self.anno=anno_di_pubblicazione

    def recente(self):
        if int(self.anno)+5>=2024:
            print('Il libro "',self.nome,'" scritto da',self.autore,"è recente perchè scritto nel",self.anno)
        else:
            print('Il libro "',self.nome,'" scritto da',self.autore,"non è recente perchè scritto nel",self.anno)
Libro1=Libro("L'ospite inquietante - Il nichilismo e i giovani","Umberto Galimberti","2007")
Libro1.recente()