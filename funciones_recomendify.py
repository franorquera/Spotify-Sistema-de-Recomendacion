from Pila import Pila
import graph_functions

def buscar_camino_minimo(grafo, cancion_inicial, cancion_final, usuarios):
    if cancion_final in usuarios or cancion_inicial in usuarios:
        print("Tanto el origen como el destino deben ser canciones")
        return
    padres, _ = graph_functions.bfs(grafo, cancion_inicial)
    if cancion_final not in padres:
        print("No se encontro recorrido")
        return
    padre = cancion_final
    pila = Pila()
    
    while padres[padre] != None:
        pila.apilar(padre)
        pila.apilar(grafo.are_linked(padre, padres[padre]))
        padre = padres[padre]
    
    pila.apilar(cancion_inicial)
    palabras = ['aparece en playlist', 'de', 'tiene una playlist', 'donde aparece']
    marcador = 0

    while not pila.esta_vacia():
        if pila.ver_tope() == cancion_final:
            print(pila.desapilar())
        else:
            print(pila.desapilar(), end=f" --> {palabras[marcador]} --> ")
        marcador += 1
        if marcador == 4: marcador = 0

def canciones_mas_importantes(dic, grafo, cant_canciones):
    pageranks = graph_functions.pagerank(grafo)
    pageranks_ordenados = []
    for cancion in pageranks:
        pageranks_ordenados.append((cancion, pageranks[cancion]))
    
    pageranks_ordenados.sort(key=_ordenar_prk, reverse=True)
    cant = int(cant_canciones)
    i = 0
    agregados = 0
    while agregados < cant:
        if pageranks_ordenados[i][0] in dic:
            i += 1
            continue
        if agregados == cant-1:
            print(pageranks_ordenados[i][0])
        else:
            print(pageranks_ordenados[i][0], end="; ")
        agregados += 1
        i+=1

def recomendacion(grafo, canciones, recomendar, cantidad_a_recomendar,dic):
    recomendacion = graph_functions.parsonalized_pagerank(grafo, canciones)
    recomendaciones_ordenadas = []
    
    for canciones in recomendacion:
        recomendaciones_ordenadas.append((canciones, recomendacion[canciones]))
    recomendaciones_ordenadas.sort(key=_ordenar_prk, reverse=True)
    
    i = 0
    agregados = 0
    cantidad = int(cantidad_a_recomendar)

    if recomendar == "canciones":
        while agregados < cantidad:
            if recomendaciones_ordenadas[i][0] in dic:
                i += 1
                continue
            if agregados == cantidad - 1:
                print(recomendaciones_ordenadas[i][0])
            else: 
                print(recomendaciones_ordenadas[i][0], end="; ")
            agregados += 1
            i += 1
            
    elif recomendar == "usuarios": 
        while agregados < cantidad:
            if recomendaciones_ordenadas[i][0] not in dic:
                i += 1
                continue
            if agregados == cantidad - 1:
                print(recomendaciones_ordenadas[i][0])
            else: 
                print(recomendaciones_ordenadas[i][0], end="; ")
            agregados += 1
            i += 1

def _ordenar_prk(tupla):
    return tupla[1]

def ciclo_n_canciones(grafo, cancion, n):
    visitados = set()
    camino = []
    if graph_functions.camino_hamiltoniano(grafo, cancion, cancion, visitados, camino, int(n)):
        for elemento in camino:
            print(elemento, end=" --> ")
        print(cancion)
    else: print("No se encontro recorrido")

def todo_en_rango(grafo, cancion, n):
    _, _, rango = graph_functions.bfs_modificado(grafo, cancion, int(n))
    print(len(rango))

def obtener_coeficiente_clustering(grafo, cancion):
    resultado = 0
    if cancion: resultado = graph_functions.coeficiente_clustering(grafo, cancion)
    else:
        for v in grafo.get_vertices():
            resultado += graph_functions.coeficiente_clustering(grafo, v)
        resultado *= 1/len(grafo.get_vertices())
    print(round(resultado, 3))