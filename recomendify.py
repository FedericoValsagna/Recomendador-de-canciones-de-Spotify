from constantes import *
from funciones_grafo import *
from recomendifutil import *

class Recomendify:

    def __init__(self, ruta_archivo):
        self.playlists = {}
        self.usuarios = set()
        self.grafo1, self.grafo2, self.playlists = generar_grafos(ruta_archivo, self.playlists, self.usuarios)
        #self.page_rank, self.ranking = page_rank(self.grafo2, ITERACIONES_PAGERANK)
        self.page_rank = None
        self.ranking = None

    def _crear_grafo_2(self):
        crear_grafo_2(self.grafo2, self.playlists)

    def _generar_pagerank(self):
        self.page_rank, self.ranking = page_rank(self.grafo2, ITERACIONES_PAGERANK)

    def camino_mas_corto(self, parametros):
        parametros = parametros.split(SEPARADOR)
        if len(parametros) != 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        cancion1 = parametros[0]
        cancion2 = parametros[1]
        if(not self.grafo1.existe_vertice(cancion1) or not self.grafo1.existe_vertice(cancion2) or cancion1 in self.usuarios or cancion2 in self.usuarios):
            print(ERROR_CANCIONES)
            return
        camino = generar_camino(self.grafo1, cancion2, cancion1)
        if not camino:
            print(ERROR_NO_RECORRIDO)
            return
        for i in range(len(camino) - 1):
            if i % 2 == 0:
                cancion_actual = camino[i]
                playlist_actual = self.grafo1.obtener_peso(camino[i], camino[i+1])[0]
                print(SALIDA_CANCION.format(cancion_actual, playlist_actual), end="")
            else:
                usuario_actual = camino[i]
                playlist_actual = self.grafo1.obtener_peso(camino[i], camino[i+1])[0]
                print(SALIDA_USUARIO.format(usuario_actual, playlist_actual), end="")
        print(camino[len(camino) - 1])
        
    def canciones_mas_importantes(self, parametros):
        if(self.grafo2.obtener_cantidad_vertices() == 0):
            self._crear_grafo_2()
        if(not self.page_rank):
            self._generar_pagerank()
        parametros = parametros.split(" ")
        if len(parametros) != 1:
            print(ERROR_PARAMETROS_CANTIDAD)
            return
        if not parametros[0].isnumeric():
            print(ERROR_NO_NUMERICO)
            return
        
        canciones = ""
        for i in range(int(parametros[0])):
            print(f"Cancion {i + 1}: {self.ranking[i]}")

    def recomendacion(self, comando):
        comando = comando.split(" ")
        if len(comando) == 0:
            print(ERROR_PARAMETROS_NULO)
            return
        if len(comando) < 3:
            print(ERROR_PARAMETROS_CANTIDAD)
            return

        if comando[0] != CANCIONES and comando[0] != USUARIOS:
            print(ERROR_PARAMETROS_INCORRECTOS)
            return

        if not comando[1].isnumeric():
            print(ERROR_NO_NUMERICO)
            return
        largo_comandos = len(comando[0]) + len(comando[1])
        modo_algoritmo = comando[0]
        cantidad_recomendaciones = int(comando[1])
        comando = " ".join(comando)
        comando = comando[largo_comandos + 2:]
        canciones = set(comando.split(SEPARADOR))
        #----------------------------------------------------------------------
        RANDOM_WALKS = 10
        LEN_WALKS = cantidad_recomendaciones * 1000
        TP_PROBABILIDAD = 0
        page_rank_per = page_rank_personalizado(self.grafo1, canciones,RANDOM_WALKS, LEN_WALKS, TP_PROBABILIDAD)
        if modo_algoritmo == CANCIONES:
            ranking = sorted([item for item in page_rank_per.keys() if self.grafo2.existe_vertice(item) and item not in canciones], key = page_rank_per.get, reverse = True)
        else:
            ranking = sorted([item for item in page_rank_per.keys() if not self.grafo2.existe_vertice(item)], key = page_rank_per.get, reverse = True)
        for i in range(cantidad_recomendaciones):
            print(f"Cancion {i + 1}: {ranking[i]}")

    def ciclo_de_n_canciones(self, parametros):
        if(self.grafo2.obtener_cantidad_vertices() == 0):
            self._crear_grafo_2()
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
            print(ERROR_NO_EXISTE_CANCION_SEG)
            return
        lista = ciclo_backtracking(self.grafo2, int(parametros[0]), parametros[1])
        if not lista:
            print(ERROR_NO_CICLO)
            return
        for can in range(len(lista) - 1):
            print(f"{lista[can]} --> ", end="")
        print(lista[len(lista) - 1])

    def todas_en_rango(self, parametros):
        if(self.grafo2.obtener_cantidad_vertices() == 0):
            self._crear_grafo_2()
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
        if(self.grafo2.obtener_cantidad_vertices() == 0):
            self._crear_grafo_2()
        if cancion:
            if not self.grafo2.existe_vertice(cancion):
                print(ERROR_NO_EXISTE_CANCION)
                return
            print(clustering(self.grafo2, cancion))
        else:
            suma = 0
            for v in self.grafo2.obtener_vertices():
                suma += clustering(self.grafo2, v)
            print(round(suma / self.grafo2.obtener_cantidad_vertices()), 3)