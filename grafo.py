class Vertice:

    def __init__(self, nombre, dato, adyacentes):
        self.dato = dato
        self.nombre = nombre
        if not adyacentes:
            adyacentes = {}
        self.adyacentes = adyacentes

class Grafo:

    def __init__(self, es_dirigido) -> None:
        self.vertices = {}
        self.es_dirigido = es_dirigido

    def __str__(self) -> str:
        pass

    def __iter__(self):
        pass

    def agregar_vertice(self, id, adyacentes, dato):
        if id in self.vertices:
            raise ValueError("El vertice ya existe")

        v = Vertice(id, dato, adyacentes)
        self.vertices[id] = v

    def borrar_vertice(self, id):
        if id not in self.vertices:
            raise ValueError("El vertice no existe")

        if self.es_dirigido:
            for v in self.vertices:
                if id in v.adyacentes:
                    v.adyacentes.pop(id)
        else:
            for id_adyacente in self.vertices[id].adyacentes.keys:
                self.vertices[id_adyacente].pop(id)

        dato = self.vertices[id].dato
        self.vertices.pop(id)
        return dato

    def cambiar_vertice(self, id, adyacentes, dato):
        pass
        
    def agregar_arista(self, id_1, id_2, peso=0):
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")
        
        if id_2 in self.vertices[id_1].adyacentes:
                raise ValueError("La arista ya existe")
        
        self.vertices[id_1].adyacentes[id_2] = peso

        if not self.es_dirigido:
            self.vertices[id_2].adyacentes[id_1] = peso
            

    def cambiar_arista(self, id_1, id_2, peso=0):
        pass

    def borrar_arista(self, id_1, id_2):
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")
        
        if id_2 not in self.vertices[id_1].adyacentes:
                raise ValueError("La arista no existe")

        self.vertices[id_1].adyacentes.pop(id_2)

        if not self.es_dirigido:
            self.vertices[id_2].adyacentes.pop(id_1)

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
