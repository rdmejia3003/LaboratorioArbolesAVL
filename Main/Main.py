from .nodo_avl import NodoAVL
from .cancion import Cancion
from .arbolavl import ArbolAVL
from .utils import getPlayList
from .TokenRequest.Request import getAccessToken
from .TokenRequest.Request import token
import requests

class Main:
    def __init__(self, token, playlist_id):
        self.arbol = ArbolAVL()
        self.token = token
        self.playlist_id = playlist_id

    def cargarPlaylist(self):
        playlist = getPlayList(self.token, self.playlist_id)

        if 'tracks' not in playlist or 'items' not in playlist['tracks']:
            print("Error al cargar la playlist o no hay canciones.")
            return
            
        for item in playlist['tracks']['items']:
            track = item['track']
            id_cancion = track['id']
            nombre = track['name']
            artistas = [artist['name'] for artist in track['artists']]
            duracion = track['duration_ms']
            popularidad = track.get('popularity', 0)

            cancion = Cancion(id_cancion, nombre, artistas, duracion, popularidad)
            self.arbol.insertar(cancion)

        print("Playlist cargada exitosamente en el árbol AVL.")

    def mostrarCanciones(self):
        print("Canciones en el árbol AVL (ordenadas por popularidad):")
        self.arbol.inOrden(self.arbol.raiz)

    def graficarArbol(self):
        self.arbol.graficar_arbol()

if __name__ == "__main__":
    main = Main(token, "17O6DGBefzwGMThjYrMLV4")
    main.cargarPlaylist()
    #main.mostrarCanciones()
    main.graficarArbol()