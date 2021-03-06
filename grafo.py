import random
from vertice import Vertice

class Grafo:

    def __init__(self, es_dirigido=False) -> None:
        self.vertices = {}
        self.es_dirigido = es_dirigido
        self.cantidad_vertices = 0
        self.cantidad_aristas = 0

    def __str__(self) -> str:
        grafo = ""
        for id, v in self.vertices.items():
            grafo += f"{id}: "
            contador = 0
            for ad in v.adyacentes.keys():
                if contador != 0:
                    grafo += ", "
                grafo += f"{ad}"
                contador += 1
            grafo += "\n"
        return grafo
        
    def agregar_vertice(self, id):
        """
        Crea un vertice en el grafo con el ID que se pase por parametro.
        Si el vertice ya existe se levanta una exepción.

        No retorna ningun valor.
        """
        if id in self.vertices:
            raise ValueError("El vertice ya existe")
        v = Vertice()
        self.vertices[id] = v
        self.cantidad_vertices += 1
 
    def borrar_vertice(self, id):
        """
        Borra el vertice correspondiente al ID pasado por parametro. 
        Si el vertice no existe se levanta una exepeción.

        No retorna ningun valor.
        """
        if id not in self.vertices:
            raise ValueError("El vertice no existe")
        if self.es_dirigido:
            for v in self.vertices.values():
                if id in v.adyacentes:
                    v.adyacentes.pop(id)
        else:
            for id_adyacente in self.vertices[id].adyacentes.keys():
                self.vertices[id_adyacente].pop(id)

        self.vertices.pop(id)
        self.cantidad_vertices -= 1
        
    def agregar_arista(self, id_1, id_2, peso=1):
        """
        Se crea una arista que une a los vertices pasados por parametros. Si el grafo es dirigido la arista va del primer vertice al segundo.
        Si no existe alguno de los vertices se levanta una exepción. Si la arista ya existe se levanta una exepción. 
        
        No retorna ningun valor.


        Parametro adicional: Peso de la arista, peso predeterminado: 1

        """
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")
        
        if id_2 in self.vertices[id_1].adyacentes:
                raise ValueError("La arista ya existe")
        
        self.vertices[id_1].adyacentes[id_2] = peso

        self.cantidad_aristas += 1

        if not self.es_dirigido:
            self.cantidad_aristas += 1
            self.vertices[id_2].adyacentes[id_1] = peso
    
    def borrar_arista(self, id_1, id_2):
        """
        Borra la arista entre los vertices pasados por parametros. Si el grafo es dirigido la arista va del primer vertice al segundo. 
        Si no existe alguno de los vertices se levanta una exepción. Si no existe la arista que se desea borrar se levanta una exepción.
        
        Devuelve el peso de la arista.
        """
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")
        
        if id_2 not in self.vertices[id_1].adyacentes:
                raise ValueError("La arista no existe")

        peso = self.vertices[id_1].adyacentes.pop(id_2)

        self.cantidad_aristas -= 1

        if not self.es_dirigido:
            self.vertices[id_2].adyacentes.pop(id_1)

        return peso

    def cambiar_peso(self, id_1, id_2, peso):
        """
        Se recibe por parametro ambos vertices que son conectados por la arista y el peso de la arista. Si el grafo es dirigido la arista va del primer vertice al segundo.
        Si no existe alguno de los vertices se levanta una exepción. Si no existe la arista se levanta una exepción.

        No retorna ningun valor la función.
        """
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
        """
        Se recibe por parametro 2 vertices y se retorna si el primero es adyacente al segundo.
        Si alguno de ambos vertices no existe se levanta una exepción.

        Se retorna un booleano indicando si existe o no la adyacencia.
        """
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")
        return id_2 in self.vertices[id_1].adyacentes

    def existe_vertice(self, id):
        """
        Se recibe por parametro un vertice y se retorna un booleano indicando si existe o no.
        """
        return id in self.vertices

    def obtener_vertice_random(self):
        """
        Devuelve un vertice aleatoreo.
        """
        return random.choice(list(self.vertices))

    def obtener_peso(self, id_1, id_2):
        """
        Recibe 2 vertices por parametro y devuelve el peso de la arista que conecta a ambos.  Si el grafo es dirigido la arista va del primer vertice al segundo.
        Si alguno de los 2 vertices no existe se levanta una exepción. Si la arista que conecta a los vertices no existe se levanta una exepción.

        Retorna el peso de dicha arista. 
        """
        if id_1 not in self.vertices:
            raise ValueError("El vertice 1 no existe")
        if id_2 not in self.vertices:
            raise ValueError("El vertice 2 no existe")
        
        if id_2 not in self.vertices[id_1].adyacentes:
                raise ValueError("La arista no existe")

        return self.vertices[id_1].adyacentes[id_2]

    def obtener_vertices(self):
        """
        Devuelve una lista que contiene a los vertices pertenecientes al grafo.
        """
        vertices = []
        for id in self.vertices.keys():
            vertices.append(id)
        return vertices

    def obtener_adyacentes(self, id):
        """
        Recibe por parametro un vertice y devuelve un diccionario con todos sus adyacentes, donde la clave es el vertice adyacente y el valor el peso de la arista que los conecta. 
        Si no existe el vertice se levanta una exepción.
        """
        if id not in self.vertices:
            raise ValueError("El vertice no existe")
        return self.vertices[id].adyacentes
    
    def obtener_cantidad_adyacentes(self, id):
        """
        Recibe por parametro un vertice y devuelve la cantidad de adyacentes de dicho vertice.
        Si el vertice no existe se levanta una exepción.
        """
        if id not in self.vertices:
            raise ValueError("El vertice no existe")
        return len(self.vertices[id].adyacentes)

    def obtener_cantidad_vertices(self):
        """
        Devuelve la cantidad de vertices que contiene el grafo.
        """
        return self.cantidad_vertices

    def obtener_cantidad_aristas(self):
        """
        Devuelve la cantidad de aristas que contiene el grafo.
        """
        return self.cantidad_aristas