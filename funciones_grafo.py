from typing import Deque
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
    q = Deque()
    q.append(id_origen)
    while not q.count() > 0:
        v = q.pop()
        for w in grafo.obtener_adyacentes(v):
            if w not in visitados:
                padres[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                q.append(w)
    return padres, orden
