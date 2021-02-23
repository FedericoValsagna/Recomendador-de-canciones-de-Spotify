from constantes import *
from funciones_grafo import *
from recomendifutil import *

class Recomendify:

    def __init__(self, ruta_archivo):
        self.grafo1, self.grafo2 = generar_grafos(ruta_archivo)
        self.page_rank, self.ranking = page_rank(self.grafo2, 1)

    def camino_mas_corto(self, parametros):
        if len(parametros) != 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return False
        cancion1 = parametros[0]
        cancion2 = parametros[1]
        if(not self.grafo1.existe_vertice(cancion1) or not self.grafo1.existe_vertice(cancion2)):
            print(ERROR_CANCIONES)
            return False
        camino = generar_camino(self.grafo1, cancion1, cancion2)

    def canciones_mas_importantes(self, parametros):
        if len(parametros) != 1:
            print(ERROR_PARAMETROS_CANTIDAD)
        if not parametros[0].isnumeric():
            print("El parametro no es numerico")
        
        for i in range(int(parametros[0])):
            print(self.ranking[i], self.page_rank[self.ranking[i]])

    def recomendacion(self, parametros):
        pass

    def ciclo_de_n_canciones(self, parametros):
        pass

    def todas_en_rango(self, parametros):
        pass

    def coeficiente_de_clustering(self, parametros):
        pass