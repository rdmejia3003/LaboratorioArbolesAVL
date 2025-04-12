class NodoAVL:
    def __init__(self, cancion):
        self.cancion = cancion
        self.izquierda = None
        self.derecha = None
        self.altura = 1
        
class Cancion:
    def __init__(self, id_cancion, nombre, artistas, duracion, popularidad):
        self.id = id_cancion
        self.nombre = nombre
        self.artistas = artistas 
        self.duracion = duracion
        self.popularidad = popularidad

    def __str__(self):
        return f"{self.nombre} - {', '.join(self.artistas)} (Popularidad: {self.popularidad})"
    
class AVLTree:

    def __init__(self):
        self.raiz = None

    def height(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balanceFactor(self, nodo):
        if not nodo:
            return 0
        return self.height(nodo.izquierda) - self.height(nodo.derecha)

    def rSI(self, nodo):
        aux = nodo.derecha
        nodo.derecha = aux.izquierda
        aux.izquierda = nodo

        nodo.balance = self.balanceFactor(nodo)
        aux.balance = self.balanceFactor(aux)
        
        return aux

    def rSD(self, nodo):
        aux = nodo.izquierda
        nodo.izquierda = aux.derecha
        aux.derecha = nodo

        nodo.balance = self.balanceFactor(nodo)
        aux.balance = self.balanceFactor(aux)
        
        return aux

    def rDI(self, nodo):
        nodo.izquierda = self.rSD(nodo.izquierda)
        return self.rSI(nodo)

    def rDD(self, nodo):
        nodo.derecha = self.rSI(nodo.derecha)
        return self.rSD(nodo)

    def addNodeAVLR(self, node, cancion):
        if not node:
            return NodoAVL(cancion)

        if node.cancion.id == cancion.id:
            print(f"El elemento {cancion.nombre} ya existe")
            return node

        if cancion.popularidad < node.cancion.popularidad:
            node.izquierda = self.addNodeAVLR(node.izquierda, cancion)
        else:
            node.derecha = self.addNodeAVLR(node.derecha, cancion)

        node.altura = 1 + max(self.height(node.izquierda), self.height(node.derecha))
        node.balance = self.balanceFactor(node)

        if node.balance == -2: 
            if node.derecha.balance == 1:
                node.derecha = self.rSD(node.derecha)
            return self.rSI(node)

        if node.balance == 2: 
            if node.izquierda.balance == -1:
                node.izquierda = self.rSI(node.izquierda)
            return self.rSD(node)

        return node

    def insertar(self, cancion):
        if not self.raiz:
            self.raiz = NodoAVL(cancion)
        else:
            self.raiz = self.addNodeAVLR(self.raiz, cancion)

    def inOrden(self, nodo):
        if nodo:
            self.inOrden(nodo.izquierda)
            print(nodo.cancion)
            self.inOrden(nodo.derecha)

    

    def graficar_arbol(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        G = nx.DiGraph()

        def agregar_nodos_edges(nodo, G, pos={}, x=0, y=0, layer=1):
            if nodo is None:
                return

            key = f"{nodo.cancion.nombre}\nPop: {nodo.cancion.popularidad}"
            pos[key] = (x, y)

            if nodo.izquierda:
                left_key = f"{nodo.izquierda.cancion.nombre}\nPop: {nodo.izquierda.cancion.popularidad}"
                G.add_edge(key, left_key)
                agregar_nodos_edges(nodo.izquierda, G, pos, x - 1 / layer, y - 1, layer + 1)

            if nodo.derecha:
                right_key = f"{nodo.derecha.cancion.nombre}\nPop: {nodo.derecha.cancion.popularidad}"
                G.add_edge(key, right_key)
                agregar_nodos_edges(nodo.derecha, G, pos, x + 1 / layer, y - 1, layer + 1)

            return pos

        pos = agregar_nodos_edges(self.raiz, G)

        plt.figure(figsize=(12, 8))
        nx.draw(
            G, pos, with_labels=True, arrows=True, node_size=2500,
            node_color="#90caf9", font_size=10, font_weight="bold"
        )
        plt.title("Árbol AVL de Canciones (por popularidad)")
        plt.show()

class Main:
    arbol = AVLTree()

    c1 = Cancion(
        id_cancion="1",
        nombre="Song A",
        artistas=["Artist 1"],
        duracion=210000,
        popularidad=75,

    )

    c2 = Cancion(
        id_cancion="2",
        nombre="Song B",
        artistas=["Artist 2"],
        duracion=180000,
        popularidad=50,
    )

    c3 = Cancion(
        id_cancion="3",
        nombre="Song C",
        artistas=["Artist 3"],
        duracion=240000,
        popularidad=80,
    )

    c4 = Cancion(
        id_cancion="4",
        nombre="Song D",
        artistas=["Artist 4"],
        duracion=200000,
        popularidad=40,
    )

    c5 = Cancion(
        id_cancion="5",
        nombre="Song E",
        artistas=["Artist 5"],
        duracion=230000,
        popularidad=90,
    )

    arbol = AVLTree()
    arbol.insertar(c1)
    arbol.insertar(c2)
    arbol.insertar(c3)
    arbol.insertar(c4)
    arbol.insertar(c5)

    print("Canciones en el árbol AVL (ordenadas por popularidad):")
    arbol.inOrden(arbol.raiz)

    arbol.graficar_arbol()
