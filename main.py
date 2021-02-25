from recomendify import Recomendify
from constantes import *
import sys

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
    
    #Borrar para la entrega
    if comando == ADYACENTES:
        recomendify.adyacentes(parametros)
def verificar_comando(comando):
    return comando in COMANDOS

def procesar_comando(recomendify):
        linea = "Aprobanos Jorge"
        while linea:
            linea = sys.stdin.readline().rstrip()
            if not linea or linea == COMANDO_QUIT or linea == COMANDO_SALIR:
                break
            linea = linea.split(" ")
            if not verificar_comando(linea[0]):
                print(ERROR_COMANDO)
                continue
            if linea[0] != CLUSTERING and len(linea) < 2:
                print(ERROR_PARAMETROS_NULO)
                continue
            comando = linea[0]
            linea = " ".join(linea[1:])
            ejecutar_comando(comando, linea, recomendify)

def main():
    ruta_archivo = sys.argv[1]
    recomendify = Recomendify(ruta_archivo)
    procesar_comando(recomendify)
    
if __name__ == "__main__":
    main()