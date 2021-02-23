from collections import deque
import random

def _dfs(grafo, v, visitados, padres, orden):
    visitados.add(v)
    a = {}
    for w in grafo.obtener_adyacentes(v).keys():
        padres[w] = v
        orden[w] = orden[v] + 1
        _dfs(grafo, w, visitados, padres, orden)

def dfs(grafo, id_origen):
    padres = {}
    orden = {}
    visitados = set()
    _dfs(grafo, id_origen, visitados, padres, orden)
    for v in grafo.obtener_vertices():
        if v not in visitados:
           _dfs(grafo, v, visitados, padres, orden) 
    return padres, orden

def bfs(grafo, id_origen):
    padres = {}
    orden = {}
    visitados = set()
    padres[id_origen] = None
    orden[id_origen] = 0
    visitados.add(id_origen)
    q = deque()
    q.appendleft(id_origen)
    while len(q) > 0:
        v = q.pop()
        for w in grafo.obtener_adyacentes(v).keys():
            if w not in visitados:
                padres[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                q.appendleft(w)
    return padres, orden

def bfs_parcial(grafo, id_origen, id_destino):
    padres = {}
    visitados = set()
    padres[id_origen] = None
    visitados.add(id_origen)
    cola = deque()
    cola.appendleft(id_origen)
    while len(cola) > 0:
        vertice = cola.pop()
        for adyacente in grafo.obtener_adyacentes(vertice).keys():
            if adyacente not in visitados:
                padres[adyacente] = vertice
                visitados.add(adyacente)
                cola.appendleft(adyacente)
                if adyacente == id_destino:
                    return padres
    return None

def camino_mas_corto(grafo, id_origen, id_destino): # BORRAR FUNCION SI NO SE USA DESPUES
    padres = bfs_parcial(grafo, id_origen, id_destino)

    camino = []
    camino.append((id_destino, padres[id_destino]))
    vertice_anterior = padres[id_destino]
    while (id_origen, None) not in camino:
        camino.append((vertice_anterior, padres[vertice_anterior]))
        vertice_anterior = padres[vertice_anterior]
    return camino

def _generar_camino(camino, padres, padre):
    if not padre:
        return
    camino.append(padre)
    _generar_camino(camino, padres, padres[padre])

def generar_camino(grafo, cancion1, cancion2):
    padres = bfs_parcial(grafo, cancion1, cancion2)
    if not padres:
        return None
    camino = []
    _generar_camino(camino, padres, cancion2)
    return camino

def _page_rank_vertice(grafo, vertice, page_rank):
    
    d = 0.85
    N = grafo.obtener_cantidad_vertices()

    sumatoria = 0
    for adyacente in grafo.obtener_adyacentes(vertice):
        sumatoria += page_rank[adyacente] / grafo.obtener_cantidad_adyacentes(adyacente)
    
    return (1.0 - d) / N  + d * sumatoria

def page_rank(grafo, iteraciones):
    page_rank = {}
    #Settear inicialmente todos los pageranks en 1
    for vertice in grafo.obtener_vertices():
        page_rank[vertice] = 1 / grafo.obtener_cantidad_vertices()
    
    for i in range(iteraciones):
        for vertice in grafo.obtener_vertices():
            page_rank[vertice] = _page_rank_vertice(grafo, vertice, page_rank)
    
    #Del diccionario crea una lista sorteada de mas popular a menos popluar
    ranking = sorted(page_rank, key = page_rank.get, reverse = True)
    return page_rank, ranking

def page_rank_personalizado(grafo, rw_cantidad, rw_largo): # rw = random_walks
    page_rank = {}
    #Settear inicialmente todos los pageranks en 1
    for vertice in grafo.obtener_vertices():
        page_rank[vertice] = 1

    #Hacer rw_cantidad numero de random walks
    for i in range (rw_cantidad):
        vertice = grafo.obtener_vertice_random()
        #Saltar rw_largo de veces de un vertice a otro adyacente aleatoreo
        for j in range(rw_largo):
            _page_rank_vertice(grafo, vertice, page_rank)
            vertice = random.choice(list(grafo.obtener_adyacentes(vertice)))

    return page_rank