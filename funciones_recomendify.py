from grafo import Grafo
from funciones_grafo import *
from constantes import *


def camino_mas_corto(grafo, parametros):
    if len(parametros) != 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return False
    cancion1 = parametros[0]
    cancion2 = parametros[1]
    if(not grafo.existe_vertice(cancion1) or not grafo.existe_vertice(cancion2)):
        print(ERROR_CANCIONES)
        return False
    camino = generar_camino(grafo, cancion1, cancion2)

def canciones_mas_importantes():
    pass

def recomendacion():
    pass

def ciclo_de_n_canciones():
    pass

def todas_en_rango():
    pass

def coeficiente_de_clustering():
    pass