from grafo import Grafo

def prueba_grafo_crear():
    grafo = Grafo(es_dirigido=True)

    assert(grafo)

def prueba_grafo_agregar_borrar_vertices():
    grafo = Grafo(es_dirigido=True)

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")

    assert(grafo.obtener_cantidad() == 2)
    for v in grafo.obtener_vertices():
        assert(v == "1" or v == "2")

    grafo.borrar_vertice("1")
    assert(grafo.obtener_cantidad() == 1)
    for v in grafo.obtener_vertices():
        assert(v == "2")

    grafo.borrar_vertice("2")
    assert(grafo.obtener_cantidad() == 0)

def prueba_grafo_aristas_adyacencia_no_dirigido():
    grafo = Grafo()

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")
    grafo.agregar_vertice("3")
    grafo.agregar_vertice("4")
    grafo.agregar_arista("1","2")
    grafo.agregar_arista("2","3")
    grafo.agregar_arista("4","1")

    assert(grafo.es_adyacente("1","2"))
    assert(not grafo.es_adyacente("1","3"))
    assert(grafo.es_adyacente("1","4"))

    assert(grafo.es_adyacente("2","1"))
    assert(grafo.es_adyacente("2","3"))
    assert(not grafo.es_adyacente("2","4"))

    assert(not grafo.es_adyacente("3","1"))
    assert(grafo.es_adyacente("3","2"))
    assert(not grafo.es_adyacente("3","4"))

    assert(grafo.es_adyacente("4","1"))
    assert(not grafo.es_adyacente("4","2"))
    assert(not grafo.es_adyacente("4","3"))
    
    grafo.borrar_arista("2","3")
    assert(not grafo.es_adyacente("2","3"))
    assert(not grafo.es_adyacente("3","2"))

def prueba_grafo_aristas_adyacencia_dirigido():
    grafo = Grafo(es_dirigido=True)

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")
    grafo.agregar_vertice("3")
    grafo.agregar_vertice("4")
    grafo.agregar_arista("1","2")
    grafo.agregar_arista("2","3")
    grafo.agregar_arista("3","2")
    grafo.agregar_arista("3","4")
    grafo.agregar_arista("4","1")

    assert(grafo.es_adyacente("1","2"))
    assert(not grafo.es_adyacente("1","3"))
    assert(not grafo.es_adyacente("1","4"))

    assert(not grafo.es_adyacente("2","1"))
    assert(grafo.es_adyacente("2","3"))
    assert(not grafo.es_adyacente("2","4"))

    assert(not grafo.es_adyacente("3","1"))
    assert(grafo.es_adyacente("3","2"))
    assert(grafo.es_adyacente("3","4"))

    assert(grafo.es_adyacente("4","1"))
    assert(not grafo.es_adyacente("4","2"))
    assert(not grafo.es_adyacente("4","3"))

    grafo.borrar_arista("2","3")
    assert(not grafo.es_adyacente("2","3"))
    assert(grafo.es_adyacente("3","2"))

def prueba_grafo_aristas_obtener_peso_no_dirigido():
    grafo = Grafo()

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")
    grafo.agregar_vertice("3")
    grafo.agregar_vertice("4")
    grafo.agregar_vertice("5")
    grafo.agregar_arista("1","2",4)
    grafo.agregar_arista("2","3",3)
    grafo.agregar_arista("4","1",-547)
    grafo.agregar_arista("3","5", 0)
    grafo.agregar_arista("1","5")

    assert(grafo.obtener_peso("1","2") == 4)
    assert(grafo.obtener_peso("2","1") == 4)
    assert(grafo.obtener_peso("2","3") == 3)
    assert(grafo.obtener_peso("3","2") == 3)
    assert(grafo.obtener_peso("4","1") == -547)
    assert(grafo.obtener_peso("1","4") == -547)
    assert(grafo.obtener_peso("3","5") == 0)
    assert(grafo.obtener_peso("5","3") == 0)
    assert(grafo.obtener_peso("1","5") == 0)
    assert(grafo.obtener_peso("5","1") == 0)

def prueba_grafo_aristas_obtener_peso_dirigido():
    grafo = Grafo(es_dirigido= True)

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")
    grafo.agregar_vertice("3")
    grafo.agregar_vertice("4")
    grafo.agregar_arista("1","2",4)
    grafo.agregar_arista("2","3",3)
    grafo.agregar_arista("3","2",0)
    grafo.agregar_arista("3","4")
    grafo.agregar_arista("4","1",-547)

    assert(grafo.obtener_peso("1","2") == 4)
    assert(grafo.obtener_peso("2","3") == 3)
    assert(grafo.obtener_peso("3","2") == 0)
    assert(grafo.obtener_peso("4","1") == -547)
    assert(grafo.obtener_peso("3","4") == 0)


def prueba_grafo_obtener_adyacentes():
    grafo = Grafo(es_dirigido=True)

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")
    grafo.agregar_vertice("3")
    grafo.agregar_vertice("4")
    grafo.agregar_arista("1","2")
    grafo.agregar_arista("2","3")
    grafo.agregar_arista("3","2")
    grafo.agregar_arista("3","4")
    grafo.agregar_arista("4","1")

    adyacentes = grafo.obtener_adyacentes("1")
    for ad in adyacentes:
        assert(grafo.es_adyacente("1", ad))

def prueba_grafo_obtener_vertices():
    grafo = Grafo(True)

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")
    grafo.agregar_vertice("3")
    grafo.agregar_vertice("4")
    grafo.agregar_arista("1","2")
    grafo.agregar_arista("2","3")
    grafo.agregar_arista("3","2")
    grafo.agregar_arista("3","4")
    grafo.agregar_arista("4","1")

    vertices = grafo.obtener_vertices()
    for v in vertices:
        assert(grafo.existe_vertice(v))

def prueba_grafo_vertice_aleatorio():
    grafo = Grafo(True)

    grafo.agregar_vertice("1")
    grafo.agregar_vertice("2")
    grafo.agregar_vertice("3")
    grafo.agregar_vertice("4")
    grafo.agregar_arista("1","2")
    grafo.agregar_arista("2","3")
    grafo.agregar_arista("3","2")
    grafo.agregar_arista("3","4")
    grafo.agregar_arista("4","1")

    iteraciones = 10

    for _ in range(iteraciones):
        assert(grafo.existe_vertice(grafo.obtener_vertice_random()))

    

def main():
    prueba_grafo_crear()
    prueba_grafo_agregar_borrar_vertices()
    prueba_grafo_aristas_adyacencia_no_dirigido()
    prueba_grafo_aristas_adyacencia_dirigido()
    prueba_grafo_aristas_obtener_peso_no_dirigido()
    prueba_grafo_aristas_obtener_peso_dirigido()
    prueba_grafo_obtener_adyacentes()
    prueba_grafo_obtener_vertices()
    prueba_grafo_vertice_aleatorio()
    print("Todo OK :)")

main()