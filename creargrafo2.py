def _crear_grafo2(grafo2, cancion, playlist, playlist_canciones_actual):
    if not grafo2.existe_vertice(cancion):
        grafo2.agregar_vertice(cancion)

    if playlist_canciones_actual[0] != playlist :
        playlist_canciones_actual[1].clear()
        playlist_canciones_actual[0] = playlist

    for track in playlist_canciones_actual[1]:
        if not grafo2.es_adyacente(cancion, track):
            grafo2.agregar_arista(cancion, track, [])

        lista_playlists = grafo2.obtener_peso(cancion, track)
        lista_playlists.append(playlist)
    playlist_canciones_actual[1].append(cancion) 
