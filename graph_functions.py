from cola import Cola
from graph import Graph
import sys
import random

def bfs(graph, origin):
    visited = set()
    parents = {}
    order = {}
    parents[origin] = None
    order[origin] = 0
    visited.add(origin)
    q = Cola()
    q.encolar(origin)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in graph.get_range(v):
            if w not in visited:
                parents[w] = v
                order[w] = order[v] + 1
                visited.add(w)
                q.encolar(w)
    return parents, order

def bfs_modificado(graph, origin, n):
    visited = set()
    parents = {}
    order = {}
    parents[origin] = None
    order[origin] = 0
    visited.add(origin)
    q = Cola()
    rango_canciones = []
    q.encolar(origin)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in graph.get_range(v):
            if w not in visited:
                parents[w] = v
                order[w] = order[v] + 1
                if order[w] == n:
                    rango_canciones.append(w)
                visited.add(w)
                q.encolar(w)
        if order[v] == n: break
    return parents, order, rango_canciones

def _dfs(graph, v, visited, parents, order):
    for w in graph.get_range(v):
        if w not in visited:
            visited.add(w)
            parents[w] = v
            order[w] = orden[v] + 1
            _dfs(graph, w, visited, parents, order)

def dfs(graph):
    visited = set()
    parents = {}
    order = {}
    for v in graph.get_vertices():
        if v not in visited:
            visited.add(v)
            parents[v] = None
            order[v] = 0
            _dfs(graph, v, visited, parents, order)
    return parents, order

def pagerank(grafo):
    coef_am = 0.85
    cant_vertices = grafo.vertex_amount()
    cte = ((1 - coef_am) / cant_vertices)
    pageranks = {}
    
    for v in grafo.get_vertices():
        pageranks[v] = 1 / cant_vertices
    
    for i in range(20):
        nuevos_ranks = {}
        for v in grafo.get_vertices():
            suma = 0
            for w in grafo.get_range(v):
                suma += (coef_am * pageranks[w]) / grafo.edge_amount(w)
            tot = cte + suma
            nuevos_ranks[v] = tot
        pageranks = nuevos_ranks
    
    return pageranks

def parsonalized_pagerank(grafo, inputs):
    recomendaciones = {}
    transferencia = 1 # Verificar
    for elemento in inputs:
        randomwalk(grafo, elemento, recomendaciones, transferencia)
    return recomendaciones

def randomwalk(grafo, inicio, dic, tansferencia):
    actual = inicio
    for i in range(10):
        if not actual in dic:
            dic[actual] = 0
        if i != 0:
            dic[actual] += tansferencia
        tansferencia = tansferencia / grafo.edge_amount(actual)
        lista = grafo.get_range(actual)
        actual = lista[random.randint(0, len(lista)-1)]

def camino_hamiltoniano(grafo, cancion, v, visitados, camino, n):
    if len(camino) == n: return _verificar(grafo, cancion, v)
    visitados.add(v)
    camino.append(v)
    for w in grafo.get_range(v):
        if w not in visitados:
            if camino_hamiltoniano(grafo, cancion, w, visitados, camino, n): return True
    visitados.remove(v)
    camino.pop()
    return False

def _verificar(grafo, cancion, v):
    return grafo.are_linked(v, cancion)

def coeficiente_clustering(grafo, cancion):
    coeficientes = {}
    adyacentes = grafo.get_range(cancion)
    if len(adyacentes) < 2: return 0
    for v in adyacentes:
        for w in adyacentes:
            if v == w: continue
            if (w, v) in coeficientes: continue
            if grafo.are_linked(v, w):
                coeficientes[(v, w)] = 1
            else:
                coeficientes[(v, w)] = 0
    suma = 0
    for numero in coeficientes.values():
        suma += numero
    return (2 * suma) / (grafo.edge_amount(cancion) * (grafo.edge_amount(cancion) - 1))
    
                