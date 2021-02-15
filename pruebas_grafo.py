from grafo import Grafo

def prueba_grafo_crear():
    grafo = Grafo(es_dirigido=True)

    assert(grafo)

def prueba_grafo_agregar_borrar_vertices():
    grafo = Grafo(es_dirigido=True)

    grafo.agregar_vertice("1", None)
    grafo.agregar_vertice("2", None)
    assert(grafo.obtener_cantidad() == 2)
    for v in grafo.obtener_vertices():
        assert(v == "1" or v == "2")
    grafo.borrar_vertice("1")
    assert(grafo.obtener_cantidad() == 1)
    for v in grafo.obtener_vertices():
        assert(v == "2")
    grafo.borrar_vertice("2")
    assert(grafo.obtener_cantidad() == 0)


def main():
    prueba_grafo_crear()
    prueba_grafo_agregar_borrar_vertices()
    print("Todo OK :)")

main()