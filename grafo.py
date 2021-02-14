class Vertice:

    def __init__(self, nombre, dato, adyacentes):
        self._dato = dato
        self._nombre = nombre
        if not adyacentes:
            adyacentes = {}
        self._adyacentes = adyacentes

    def nombre(self):
        return self._nombre

    def dato(self):
        return self._dato
        
    def adyacentes(self):
        return self._adyacentes

class Grafo:

    def __init__(self, es_dirigido) -> None:
        self.vertices = {}
        self.es_dirigido = es_dirigido

    def __str__(self) -> str:
        pass

    def __iter__(self):
        pass

    def agregar_vertice(self, adyacentes, dato, id):
        if id in self.vertices:
            raise ValueError("El vertice ya existe en el grafo")
        v = Vertice(id, dato, adyacentes)
        self.vertices[id] = v

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
