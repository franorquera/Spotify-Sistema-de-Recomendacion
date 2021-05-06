#!/usr/bin/python3
from graph import Graph
from Pila import Pila
import graph_functions
import funciones_recomendify
import sys

CAMINO = "camino"
MAS_IMPORTANTES = "mas_importantes"
RECOMENDACION = "recomendacion"
CICLO = "ciclo"
RANGO = "rango"
CLUSTERING = "clustering"


def inicializacion():
    grafo_usuario_cancion = Graph()
    grafo_playlist_cancion = Graph()
    return grafo_usuario_cancion, grafo_playlist_cancion

def guardar_datos(usuarios, canciones, grafo_usuarios, grafos_playlists, archivo):
    with open(archivo) as spotify:
        spotify.readline()
        for linea in spotify:
            linea = linea.rstrip()
            _id, user_id, track_name, artist, playlist_id, playlist_name, genres = linea.split('\t')
            usuarios.add(user_id)
            grafo_usuarios.add_vertex(user_id)
            track = track_name + ' - ' + artist
            grafo_usuarios.add_vertex(track)
            grafo_usuarios.add_edge(user_id, track, playlist_name)

            if not playlist_name in canciones:
                canciones[playlist_name] = []
            canciones[playlist_name].append(track)

def llenar_grafo_playlist(grafos_playlists, canciones):
    for playlist in canciones:
        for cancion in canciones[playlist]: 
            grafos_playlists.add_vertex(cancion)
        for cancion in canciones[playlist]:
            for otras_cancion in canciones[playlist]:
                if cancion == otras_cancion: continue
                grafos_playlists.add_edge(cancion, otras_cancion, playlist)

def leer_lineas(usuarios, grafo_usuario_cancion, grafo_playlist_cancion, canciones):
    for linea in sys.stdin:
        linea = linea.rstrip()
        procesar_linea(usuarios, linea, grafo_usuario_cancion, grafo_playlist_cancion, canciones)

def procesar_linea(usuarios,linea, grafo_usuario_cancion, grafo_playlist_cancion, canciones):
    lineas = linea.split()
    comando = lineas.pop(0)
    if comando in (CICLO, RANGO, CLUSTERING) and grafo_playlist_cancion.vertex_amount() == 0: 
        llenar_grafo_playlist(grafo_playlist_cancion, canciones)

    if comando == CAMINO:
        lineas = " ".join(lineas)
        canciones = lineas.split(' >>>> ')
        funciones_recomendify.buscar_camino_minimo(grafo_usuario_cancion, canciones[0], canciones[1], usuarios)
    if comando == MAS_IMPORTANTES:
        cantidad_canciones = lineas[0]
        funciones_recomendify.canciones_mas_importantes(usuarios,grafo_usuario_cancion, cantidad_canciones)
    if comando == RECOMENDACION:
        recomendar = lineas.pop(0)
        cantidad_a_recomendar = lineas.pop(0)
        lineas = " ".join(lineas)
        canciones = lineas.split(' >>>> ')
        funciones_recomendify.recomendacion(grafo_usuario_cancion, canciones, recomendar, cantidad_a_recomendar, usuarios)
    if comando == CICLO:
        n = lineas.pop(0)
        cancion = " ".join(lineas)
        funciones_recomendify.ciclo_n_canciones(grafo_playlist_cancion, cancion, n)
    if comando == RANGO:
        n = lineas.pop(0)
        cancion = " ".join(lineas)
        funciones_recomendify.todo_en_rango(grafo_playlist_cancion, cancion, n)
    if comando == CLUSTERING:
        cancion = " ".join(lineas)
        funciones_recomendify.obtener_coeficiente_clustering(grafo_playlist_cancion, cancion)

def main():
    usuarios = set()
    canciones = {}
    grafo_usuario_cancion, grafo_playlist_cancion = inicializacion()
    guardar_datos(usuarios, canciones, grafo_usuario_cancion, grafo_playlist_cancion, sys.argv[1])
    leer_lineas(usuarios, grafo_usuario_cancion, grafo_playlist_cancion, canciones)
    
main()