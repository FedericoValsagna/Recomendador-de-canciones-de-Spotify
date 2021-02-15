import random
from vertice import Vertice

class Grafo:

    def __init__(self, es_dirigido=False) -> None:
        self.vertices = {}
        self.es_dirigido = es_dirigido
        self.cantidad = 0

    def __str__(self) -> str:
        pass

    def agregar_vertice(self, id, dato):
        if id in self.vertices:
            raise ValueError("El vertice ya existe")
        v = Vertice(dato)
        self.vertices[id] = v
        self.cantidad += 1
 
    def borrar_vertice(self, id):
        if id not in self.vertices:
            raise ValueError("El vertice no existe")
        culo = {}
        if self.es_dirigido:
            for v in self.vertices.values():
                if id in v.adyacentes:
                    v.adyacentes.pop(id)
        else:
            for id_adyacente in self.vertices[id].adyacentes.keys():
                self.vertices[id_adyacente].pop(id)

        dato = self.vertices[id].dato
        self.vertices.pop(id)
        self.cantidad -= 1
        return dato
    
    def cambiar_dato(self, id, dato):
        if id not in self.vertices:
            raise ValueError("El vertice no existe")

        self.vertices[id].dato = dato
        
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

    def cambiar_peso(self, id_1, id_2, peso):
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")

        if id_2 not in self.vertices[id_1].adyacentes:
                raise ValueError("La arista no existe")

        self.vertices[id_1].adyacentes[id_2] = peso

        if not self.es_dirigido:
            self.vertices[id_2].adyacentes[id_1] = peso

    def es_adyacente(self, id_1, id_2):
        return id_2 in self.vertices[id_1].adyacentes

    def existe_vertice(self, id):
        return id in self.vertices

    def obtener_vertice_random(self):
        return random.choice(list(self.vertices))

    def obtener_dato(self, id):
        if id not in self.vertices:
            raise ValueError("El vertice no existe")
        return self.vertices[id].dato

    def obtener_peso(self, id_1, id_2):
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")
        
        if id_2 not in self.vertices[id_1].adyacentes:
                raise ValueError("La arista no existe")

        return self.vertices[id_1].adyacentes[id_2]

    def obtener_vertices(self):
        vertices = []
        for id in self.vertices.keys():
            vertices.append(id)
        return vertices

    def obtener_adyacentes(self, id):
        if id not in self.vertices:
            raise ValueError("El vertice no existe")
        adyacentes = []
        for id in self.vertices[id].adyacentes.keys():
            adyacentes.append(id)
        return adyacentes

    def obtener_cantidad(self):
        return self.cantidad