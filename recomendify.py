from grafo import Grafo
from funciones_grafo import bfs, dfs
import sys
from constantes import *



def _generar_camino(camino, padres, padre):
    if not padre:
        return
    camino.append(padre)
    _generar_camino(camino, padres, padres[padre])

def generar_camino(grafo, cancion1, cancion2):
    padres, _ = bfs(grafo, cancion2)
    camino = []
    _generar_camino(camino, padres, cancion1)
    print(camino)

def ejecutar_comando(comando, parametros, grafo1, grafo2):
    parametros = parametros.split(SEPARADOR)
    if comando == CAMINO:
        if len(parametros) != 2:
            print(ERROR_PARAMETROS_CANTIDAD)
            return False
        cancion1 = parametros[0]
        cancion2 = parametros[1]
        if(not grafo1.existe_vertice(cancion1) or not grafo1.existe_vertice(cancion2)):
            print(ERROR_CANCIONES)
            return False
        generar_camino(grafo1, cancion1, cancion2)

    if comando == MAS_IMPORTANTES:
        pass
    
    if comando == RECOMENDACION:
        pass

    if comando == CICLO:
        pass

    if comando == RANGO:
        pass
    
    if comando == CLUSTERING:
        pass

def verificar_comando(comando):
    return comando in COMANDOS

def procesar_comando(grafo1, grafo2):
        linea = "First"
        while linea:
            linea = sys.stdin.readline().rstrip()
            if not linea:
                break
            linea = linea.split(" ")
            if not verificar_comando(linea[0]):
                print(ERROR_COMANDO)
                continue
            if len(linea) < 2:
                print(ERROR_PARAMETROS_NULO)
                continue
            comando = linea[0]
            linea = " ".join(linea[1:])
            ejecutar_comando(comando, linea, grafo1, grafo2)

def procesar_archivo(ruta, grafo1, grafo2):
    with open(ruta, encoding = "utf8") as archivo:
        archivo.readline() # 2 veces para no usar el header del archivo
        linea = archivo.readline()
        canciones_anteriores = []
        playlist_actual = None
        while linea:     # linea != ''
            linea = linea.rstrip('\n')
            linea = linea.split('\t')
            
            playlist = linea[PLAYLIST_ID]
            if playlist_actual != playlist:
                canciones_anteriores.clear()
                playlist_actual = playlist
            
            procesar_linea(linea, grafo1, grafo2, canciones_anteriores)
            linea = archivo.readline()

def procesar_linea(linea, grafo1, grafo2, canciones_anteriores):
    cancion = " - ".join((linea[TRACK_NAME], linea[ARTIST]))
    usuario = linea[USER_ID]
    playlist = (linea[PLAYLIST_ID], linea[PLAYLIST_NAME])
    crear_grafo1(grafo1, linea, cancion, usuario, playlist)
    crear_grafo2(grafo2, cancion, playlist, canciones_anteriores)

def crear_grafo1(grafo1, linea, cancion, usuario, playlist):
    if not grafo1.existe_vertice(usuario):
        grafo1.agregar_vertice(usuario)
    
    if not grafo1.existe_vertice(cancion):
        grafo1.agregar_vertice(cancion)

    if not grafo1.es_adyacente(usuario, cancion):
        grafo1.agregar_arista(usuario, cancion, [])
    
    lista_playlists = grafo1.obtener_peso(usuario, cancion)
    lista_playlists.append(playlist)

def crear_grafo2(grafo2, cancion, playlist, canciones_anteriores):
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

    print("Cargando datos...")
    procesar_archivo(ruta_archivo, grafo1, grafo2)

    print("Esperando comandos: ")
    procesar_comando(grafo1, grafo2)
    


if __name__ == "__main__":
    main()