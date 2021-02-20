class Cancion:
    def __init__(self, nombre, artista, genero):
        self.nombre = nombre
        self.artista = artista
        self.genero = genero

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.nombre, self.artista))



cancion1 = Cancion("Eraser", "Ed Sheeran", "Pop")

dic ={}
dic[cancion1] = "Hola"
print(dic)