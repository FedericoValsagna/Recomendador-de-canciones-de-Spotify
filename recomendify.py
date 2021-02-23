from grafo import Grafo
from constantes import *
from funciones_grafo import *

class Recomendify:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.grafo1 = Grafo()
        self.grafo2 = Grafo()
        self._canciones_anteriores = []
        self._playlist_actual = None
        self._procesar_archivo()
    
    def _procesar_archivo(self):
        with open(self.ruta_archivo, encoding = "utf8") as archivo:
            archivo.readline() # 2 veces para no usar el header del archivo
            linea = archivo.readline()
            while linea:
                linea = linea.rstrip('\n')
                linea = linea.split('\t')
                self._procesar_linea(linea)
                linea = archivo.readline()

    def _procesar_linea(self, linea):
        cancion = " - ".join((linea[TRACK_NAME], linea[ARTIST]))
        usuario = linea[USER_ID]
        playlist = (linea[PLAYLIST_ID], linea[PLAYLIST_NAME])
        self._crear_grafo1(linea, cancion, usuario, playlist)
        self._crear_grafo2(cancion, playlist)

    def _crear_grafo1(self, linea, cancion, usuario, playlist):
        if not self.grafo1.existe_vertice(usuario):
            self.grafo1.agregar_vertice(usuario)

        if not self.grafo1.existe_vertice(cancion):
            self.grafo1.agregar_vertice(cancion)

        if not self.grafo1.es_adyacente(usuario, cancion):
            self.grafo1.agregar_arista(usuario, cancion, [])

        lista_playlists = self.grafo1.obtener_peso(usuario, cancion)
        lista_playlists.append(playlist)

    def _crear_grafo2(self, cancion, playlist):
        if not self.grafo2.existe_vertice(cancion):
            self.grafo2.agregar_vertice(cancion)

        if (self._playlist_actual != playlist):
            self._canciones_anteriores.clear()
            self._playlist_actual = playlist

        for track in self._canciones_anteriores:
            if not self.grafo2.es_adyacente(cancion, track):
                self.grafo2.agregar_arista(cancion, track, [])

            lista_playlists = self.grafo2.obtener_peso(cancion, track)
            lista_playlists.append(playlist)
        self._canciones_anteriores.append(cancion)

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
        pass

    def recomendacion(self, parametros):
        pass

    def ciclo_de_n_canciones(self, parametros):
        pass

    def todas_en_rango(self, parametros):
        pass

    def coeficiente_de_clustering(self, parametros):
        pass