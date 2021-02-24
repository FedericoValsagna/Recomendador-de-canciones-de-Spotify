from constantes import *
from funciones_grafo import *
from recomendifutil import *

class Recomendify:

    def __init__(self, ruta_archivo):
        print("Generando grafos...")
        self.grafo1, self.grafo2 = generar_grafos(ruta_archivo)
        print("Generando page_rank...")
        self.page_rank, self.ranking = page_rank(self.grafo2, ITERACIONES_PAGERANK)
        print("Recomendify listo para usar!")

    def camino_mas_corto(self, parametros):
        parametros = parametros.split(SEPARADOR)
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
        if not parametros.isnumeric():
            print(ERROR_NO_NUMERICO)
            return
        
        canciones = ""
        for i in range(int(parametros)):
            canciones += f"{self.ranking[i]}; "
        print(canciones[:-2]) # Slice para que que no este el ultimo '; '

    def recomendacion(self, parametros):
        print(parametros)
        modo_algoritmo = parametros[0]
        cantidad_recomendaciones = parametros[1]
        canciones = parametros[2].split(SEPARADOR)

        pass

    def ciclo_de_n_canciones(self, parametros):
        parametros = parametros.split(" ")
        if len(parametros) < 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        n = parametros[0]
        if not n.isnumeric():
            print(ERROR_NO_NUMERICO)
            return
        cancion = " ".join(parametros[1:])
        parametros = (n, cancion)
        if len(parametros) != 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        if not self.grafo2.existe_vertice(parametros[1]):
            print(ERROR_NO_EXISTE_CANCION)
            return
        lista = ciclo_backtracking(self.grafo2, int(parametros[0]), parametros[1])
        if not lista:
            print(ERROR_NO_CICLO)
            return
        print(lista)

    def todas_en_rango(self, parametros):
        parametros = parametros.split(" ")
        if len(parametros) < 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        n = parametros[0]
        if not n.isnumeric():
            print(ERROR_NO_NUMERICO)
            return
        cancion = " ".join(parametros[1:])
        parametros = (n, cancion)
        if len(parametros) != 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        if not self.grafo2.existe_vertice(parametros[1]):
            print(ERROR_NO_EXISTE_CANCION)
            return
        orden = bfs_parcial_orden(self.grafo2, parametros[1], int(n))
        canciones_a_n_distancia = []
        for v in orden:
            if orden[v] == int(n):
                canciones_a_n_distancia.append(v)
        print(len(canciones_a_n_distancia))

    def coeficiente_de_clustering(self, cancion):
        if cancion:
            if len(cancion) > 1:
                print(ERROR_PARAMETROS_CANTIDAD)
                return
            if not self.grafo2.existe_vertice(cancion):
                print(ERROR_NO_EXISTE_CANCION)
                return
            print(clustering(self.grafo2, cancion))
        else:
            suma = 0
            for v in self.grafo2.obtener_vertices():
                suma += clustering(self.grafo2, v)
            print(round(suma / self.grafo2.obtener_cantidad_vertices()), 3)