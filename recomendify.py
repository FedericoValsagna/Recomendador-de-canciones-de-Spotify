from grafo import Grafo
from funciones_grafo import bfs, dfs
import sys

ID = 0
USER_ID = 1
TRACK_NAME = 2
ARTIST = 3
PLAYLIST_ID = 4
PLAYLIST_NAME = 5
GENRES = 6

def procesar_archivo(ruta, grafo1, grafo2):
    with open(ruta, encoding = "utf8") as archivo:
        archivo.readline() # 2 veces para no usar el header del archivo
        linea = archivo.readline()
        canciones_anteriores = []
        playlist_actual = None
        while linea:     # linea != ''
            linea = linea.rstrip('\n')
            linea = linea.split('\t')

            playlist = (linea[PLAYLIST_ID], linea[PLAYLIST_NAME])
            if playlist_actual != playlist:
                canciones_anteriores.clear()
                playlist_actual = playlist
            
            procesar_linea(linea, grafo1, grafo2, canciones_anteriores, playlist, playlist_actual)
            linea = archivo.readline()

    
    
def procesar_linea(linea, grafo1, grafo2, canciones_anteriores, playlist, playlist_actual):
    cancion = " - ".join((linea[TRACK_NAME], linea[ARTIST]))
    usuario = linea[USER_ID]
    crear_grafo1(grafo1, linea, cancion, usuario, playlist)
    crear_grafo2(grafo2, cancion, playlist, canciones_anteriores, playlist_actual)

def crear_grafo1(grafo1, linea, cancion, usuario, playlist):
    if not grafo1.existe_vertice(usuario):
        grafo1.agregar_vertice(usuario)
    
    if not grafo1.existe_vertice(cancion):
        grafo1.agregar_vertice(cancion)

    if not grafo1.es_adyacente(usuario, cancion):
        grafo1.agregar_arista(usuario, cancion, [])
    
    lista_playlists = grafo1.obtener_peso(usuario, cancion)
    lista_playlists.append(playlist)

def crear_grafo2(grafo2, cancion, playlist, canciones_anteriores, playlist_actual):
    if not grafo2.existe_vertice(cancion):
        grafo2.agregar_vertice(cancion)

    for track in canciones_anteriores:
        if not grafo2.es_adyacente(cancion, track):
            grafo2.agregar_arista(cancion, track, [])
        
        lista_playlists = grafo2.obtener_peso(cancion, track)
        lista_playlists.append(playlist)
    canciones_anteriores.append(cancion)


def main():
    ruta_archivo = sys.argv[1]

    grafo1 = Grafo()
    grafo2 = Grafo()
    procesar_archivo(ruta_archivo, grafo1, grafo2)
    


if __name__ == "__main__":
    main()

