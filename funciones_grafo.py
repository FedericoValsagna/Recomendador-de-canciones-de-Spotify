from grafo import Grafo
from collections import deque

def _dfs(grafo, v, visitados, padres, orden):
    visitados.add(v)
    for w in grafo.obtener_adyacentes(v):
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
        for w in grafo.obtener_adyacentes(v):
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
        for adyacente in grafo.obtener_adyacentes(vertice):
            if adyacente not in visitados:
                padres[adyacente] = vertice
                visitados.add(adyacente)
                cola.appendleft(adyacente)
                if adyacente == id_destino:
                    return padres

def camino_mas_corto(grafo, id_origen, id_destino):
    padres = bfs_parcial(grafo, id_origen, id_destino)

    camino = []
    camino.append((id_destino, padres[id_destino]))
    vertice_anterior = padres[id_destino]
    while (id_origen, None) not in camino:
        camino.append((vertice_anterior, padres[vertice_anterior]))
        vertice_anterior = padres[vertice_anterior]
    return camino
                
