from grafo import Grafo

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