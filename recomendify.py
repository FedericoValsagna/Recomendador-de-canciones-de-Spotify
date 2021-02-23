from constantes import *
from funciones_grafo import *
from recomendifutil import *

class Recomendify:

    def __init__(self, ruta_archivo):
        self.grafo1, self.grafo2 = generar_grafos(ruta_archivo)
        self.page_rank, self.ranking = page_rank(self.grafo2, ITERACIONES_PAGERANK)

    def camino_mas_corto(self, parametros):
        if len(parametros) != 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        cancion1 = parametros[0]
        cancion2 = parametros[1]
        if(not self.grafo2.existe_vertice(cancion1) or not self.grafo2.existe_vertice(cancion2)):
            print(ERROR_CANCIONES)
            return
        camino = generar_camino(self.grafo1, cancion2, cancion1)
        if not camino:
            print(ERROR_NO_RECORRIDO)
            return
        for i in range(len(camino) - 1):
            if i % 2 == 0:
                cancion_actual = camino[i]
                playlist_actual = self.grafo1.obtener_peso(camino[i], camino[i+1])[0][OFFSET_PLAYLIST_NAME]
                print(SALIDA_CANCION.format(cancion_actual, playlist_actual), end="")
            else:
                usuario_actual = camino[i]
                playlist_actual = self.grafo1.obtener_peso(camino[i], camino[i+1])[0][OFFSET_PLAYLIST_NAME]
                print(SALIDA_USUARIO.format(usuario_actual, playlist_actual), end="")
        print(camino[len(camino)- 1])

    def canciones_mas_importantes(self, parametros):
        if len(parametros) != 1:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        if not parametros[0].isnumeric():
            print(ERROR_NO_NUMERICO)
            return
        
        canciones = ""
        for i in range(int(parametros[0])):
            canciones += f"{self.ranking[i]}; "
        print(canciones[:-2]) # Slice para que que no este el ultimo '; '

    def recomendacion(self, parametros):
        pass

    def ciclo_de_n_canciones(self, parametros):
        pass

    def todas_en_rango(self, parametros):
        pass

    def coeficiente_de_clustering(self, parametros):
        pass