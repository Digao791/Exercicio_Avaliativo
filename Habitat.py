from Cuidador import Cuidador



class Habitat:

    id : str
    def __init__(self, nome: str, tipoAmbiente: str, cuidador: Cuidador):
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador
