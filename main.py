from recomendify import Recomendify
from grafo import Grafo 
import sys
from constantes import *
from funciones_recomendify import *


def ejecutar_comando(comando, parametros, recomendify):
    if comando == CAMINO:
        recomendify.camino_mas_corto(parametros)

    if comando == MAS_IMPORTANTES:
        recomendify.canciones_mas_importantes(parametros)
    
    if comando == RECOMENDACION:
        recomendify.recomendacion(parametros)

    if comando == CICLO:
        recomendify.ciclo_de_n_canciones(parametros)

    if comando == RANGO:
        recomendify.todas_en_rango(parametros)
    
    if comando == CLUSTERING:
        recomendify.coeficiente_de_clustering(parametros)
    

def verificar_comando(comando):
    return comando in COMANDOS

def procesar_comando(recomendify):
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
            parametros = linea.split(SEPARADOR)
            ejecutar_comando(comando, parametros, recomendify)

def main():
    ruta_archivo = sys.argv[1]

    print("Cargando datos...")
    recomendify = Recomendify(ruta_archivo)

    print("Esperando comandos: ")
    procesar_comando(recomendify)
    

if __name__ == "__main__":
    main()