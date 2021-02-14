class Vertice:

    def __init__(self, adyacentes, dato):
<<<<<<< HEAD
        self._dato = dato
        if not adyacentes:
            adyacentes = {}
        self._adyacentes = adyacentes
=======
        self.dato = dato
>>>>>>> 28bed956b28a3bcba7a00a463fca553a06daf4d8

    def dato(self):
        return self._dato

    def adyacentes(self):
        return self._adyacentes

class Grafo:

    def __init__() -> None:
        pass

    def __str__(self) -> str:
        pass

    def __iter__(self):
        pass

    def agregar_vertice(self, Vertice):
        pass

    def borrar_vertice(self):
        pass

    def agregar_arista(self):
        pass

    def borrar_arista(self):
        pass

    def es_adyacentes(self, v1, v2):
        pass

    def existe_vertice(self, id):
        pass

    def obtener_vertice_random(self):
        pass

    def vertices(self):
        pass

    def adyacentes(self, v):
        pass
