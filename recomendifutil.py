from grafo import Grafo
from constantes import *

def generar_grafos(ruta_archivo):
    grafo1 = Grafo()
    grafo2 = Grafo()
    playlists = {}
    _procesar_archivo(ruta_archivo, grafo1, playlists)
    crear_grafo_2(grafo2, playlists)
    return grafo1, grafo2, playlists

def _procesar_archivo(ruta_archivo, grafo1, playlists):
    with open(ruta_archivo, encoding = "utf8") as archivo:
        archivo.readline() # 2 veces para no usar el header del archivo
        linea = archivo.readline()
        while linea:
            linea = linea.rstrip('\n')
            linea = linea.split(SEPARADOR_ARCHIVO)
            _procesar_linea(linea, grafo1, playlists)
            linea = archivo.readline()

def _procesar_linea(linea, grafo1, playlists):
    cancion = " - ".join((linea[TRACK_NAME], linea[ARTIST]))
    usuario = linea[USER_ID]
    playlist = linea[PLAYLIST_NAME]
    canciones = playlists.get(playlist, [])
    canciones.append(cancion)
    playlists[playlist] = canciones
    _crear_grafo1(grafo1, linea, cancion, usuario, playlist)

def _crear_grafo1(grafo1, linea, cancion, usuario, playlist):
    if not grafo1.existe_vertice(usuario):
        grafo1.agregar_vertice(usuario)

    if not grafo1.existe_vertice(cancion):
        grafo1.agregar_vertice(cancion)

    if not grafo1.es_adyacente(usuario, cancion):
        grafo1.agregar_arista(usuario, cancion, [])

    lista_playlists = grafo1.obtener_peso(usuario, cancion)
    lista_playlists.append(playlist)

def crear_grafo_2(grafo2, playlists):
    for playlist, canciones in playlists.items():
        for i in range(len(canciones) - 1):
            if not grafo2.existe_vertice(canciones[i]):
                grafo2.agregar_vertice(canciones[i])
            for j in range(i + 1, len(canciones)):
                if not grafo2.existe_vertice(canciones[j]):
                    grafo2.agregar_vertice(canciones[j])
                if not grafo2.es_adyacente(canciones[i], canciones[j]):
                    grafo2.agregar_arista(canciones[i], canciones[j])