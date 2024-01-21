class spotify:
    def __init__(self,nome_canzone,durata,album,artista):
        self.nome=nome_canzone
        self.durata=durata
        self.album=album
        self.artista=artista
    def traccia(self):
        print("Hai ascoltato",self.nome,"per",self.durata,
              "secondi, che fa parte dell'album",
              self.album,"ed è stata scritta da",self.artista)
traccia=spotify("LORO",199,"Noi, loro, gli altri","Marracash")
traccia.traccia()