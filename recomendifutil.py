from grafo import Grafo
from constantes import *

def generar_grafos(ruta_archivo):
    grafo1 = Grafo()
    grafo2 = Grafo()

    playlist_canciones_actual = [None, []] # Primer elemento: ID playlist actual. Segundo: lista de canciones de playlist actual
    _procesar_archivo(ruta_archivo, grafo1, grafo2, playlist_canciones_actual)
    return grafo1, grafo2

def _procesar_archivo(ruta_archivo, grafo1, grafo2, playlist_canciones_actual):
    with open(ruta_archivo, encoding = "utf8") as archivo:
        archivo.readline() # 2 veces para no usar el header del archivo
        linea = archivo.readline()
        while linea:
            linea = linea.rstrip('\n')
            linea = linea.split('\t')
            _procesar_linea(linea, grafo1, grafo2, playlist_canciones_actual)
            linea = archivo.readline()

def _procesar_linea(linea, grafo1, grafo2, playlist_canciones_actual):
    cancion = " - ".join((linea[TRACK_NAME], linea[ARTIST]))
    usuario = linea[USER_ID]
    playlist = (linea[PLAYLIST_ID], linea[PLAYLIST_NAME])
    _crear_grafo1(grafo1, linea, cancion, usuario, playlist)
    _crear_grafo2(grafo2, cancion, playlist, playlist_canciones_actual)

def _crear_grafo1(grafo1, linea, cancion, usuario, playlist):
    if not grafo1.existe_vertice(usuario):
        grafo1.agregar_vertice(usuario)

    if not grafo1.existe_vertice(cancion):
        grafo1.agregar_vertice(cancion)

    if not grafo1.es_adyacente(usuario, cancion):
        grafo1.agregar_arista(usuario, cancion, [])

    lista_playlists = grafo1.obtener_peso(usuario, cancion)
    lista_playlists.append(playlist)

def _crear_grafo2(grafo2, cancion, playlist, playlist_canciones_actual):
    if not grafo2.existe_vertice(cancion):
        grafo2.agregar_vertice(cancion)

    if (playlist_canciones_actual[0] != playlist):
        playlist_canciones_actual[1].clear()
        playlist_canciones_actual[0] = playlist

    for track in playlist_canciones_actual[1]:
        if not grafo2.es_adyacente(cancion, track):
            grafo2.agregar_arista(cancion, track, [])

        lista_playlists = grafo2.obtener_peso(cancion, track)
        lista_playlists.append(playlist)
    playlist_canciones_actual[1].append(cancion)