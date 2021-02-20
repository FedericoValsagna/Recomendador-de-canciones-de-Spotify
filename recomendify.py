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
    with open(ruta) as archivo:
        linea = archivo.readline()
        while linea:     # linea != ''
            linea = linea.rstrip('\n')
            linea = linea.split('   ')
            procesar_linea(linea, grafo1, grafo2)

def procesar_linea(linea, grafo1, grafo2):

    cancion = " - ".join((linea[TRACK_NAME], linea[ARTIST]))
    usuario = linea[USER_ID]
    #Grafo1
    if not grafo1.existe_vertice(usuario):
        grafo1.agregar_vertice(usuario)
    
    if not grafo1.existe_vertice(cancion):
        grafo1.agregar_vertice(cancion)     # Genres as dato

    if not grafo1.es_adyacente(usuario, cancion):
        grafo1.agregar_arista(usuario, cancion, [])
    
    lista_playlists = grafo1.obtener_peso(usuario, cancion)
    playlist = (linea[PLAYLIST_ID], linea[PLAYLIST_NAME])
    lista_playlists.append((playlist)
    #Grafo2

def main():
    ruta_archivo = sys.argv[1]

    grafo1 = Grafo()
    grafo2 = Grafo()
    procesar_archivo(ruta_archivo, grafo1, grafo2)
    


if __name__ == "__main__":
    main()

