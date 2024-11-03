import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2, peso):
        self.grafo[vertice1].append((vertice2, peso))
        self.grafo[vertice2].append((vertice1, peso))  # No dirigido

    def prim_mst(self):
        mst = []
        visitados = set()
        total_cost = 0
        initial_vertex = next(iter(self.grafo))
        min_heap = [(0, initial_vertex, None)]

        while min_heap and len(visitados) < len(self.grafo):
            peso, actual, previo = heapq.heappop(min_heap)
            if actual not in visitados:
                visitados.add(actual)
                if previo is not None:
                    mst.append((previo, actual, peso))
                    total_cost += peso
                for vecino, p in self.grafo[actual]:
                    if vecino not in visitados:
                        heapq.heappush(min_heap, (p, vecino, actual))
        
        return mst, total_cost

    def dijkstra(self, inicio, destino):
        min_heap = [(0, inicio)]
        distancias = {v: float('inf') for v in self.grafo}
        distancias[inicio] = 0
        padres = {v: None for v in self.grafo}

        while min_heap:
            dist_actual, vertice_actual = heapq.heappop(min_heap)

            if vertice_actual == destino:
                camino = []
                while vertice_actual:
                    camino.append(vertice_actual)
                    vertice_actual = padres[vertice_actual]
                camino.reverse()
                return distancias[destino], camino

            for vecino, peso in self.grafo[vertice_actual]:
                distancia = dist_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    padres[vecino] = vertice_actual
                    heapq.heappush(min_heap, (distancia, vecino))

        return None, None


# Instancia del grafo
grafo = Grafo()

# Vértices (ambientes de la casa)
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", 
             "habitación 2", "sala de estar", "terraza", "patio"]

for ambiente in ambientes:
    grafo.agregar_vertice(ambiente)

# Aristas y pesos (distancias en metros entre ambientes)
grafo.agregar_arista("cocina", "comedor", 5)
grafo.agregar_arista("cocina", "baño 1", 3)
grafo.agregar_arista("cocina", "terraza", 7)
grafo.agregar_arista("comedor", "baño 1", 4)
grafo.agregar_arista("comedor", "sala de estar", 6)
grafo.agregar_arista("comedor", "habitación 1", 8)
grafo.agregar_arista("baño 1", "quincho", 9)
grafo.agregar_arista("baño 1", "habitación 1", 2)
grafo.agregar_arista("sala de estar", "habitación 1", 10)
grafo.agregar_arista("sala de estar", "habitación 2", 12)
grafo.agregar_arista("habitación 1", "habitación 2", 1)
grafo.agregar_arista("habitación 2", "patio", 5)
grafo.agregar_arista("terraza", "patio", 3)
grafo.agregar_arista("cocina", "quincho", 4)  # Arista adicional para cumplir el requisito
grafo.agregar_arista("comedor", "cochera", 6)  # Arista adicional para cumplir el requisito

# Árbol de expansión mínima
mst, total_cost = grafo.prim_mst()
print("Árbol de expansión mínima (MST):", mst)
print("Metros de cable necesarios para el MST:", total_cost)

# Camino más corto entre "habitación 1" y "sala de estar"
distancia_cable, camino_corto = grafo.dijkstra("habitación 1", "sala de estar")
print("Metros de cable necesarios para conectar habitación 1 a sala de estar:", distancia_cable)
print("Camino más corto desde habitación 1 a sala de estar:", " -> ".join(camino_corto))
