class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_personaje(self, personaje):
        if personaje.nombre not in self.vertices:
            self.vertices[personaje.nombre] = personaje
            self.aristas[personaje.nombre] = {}

    def agregar_relacion(self, personaje1, personaje2, episodios):
        if personaje1.nombre in self.vertices and personaje2.nombre in self.vertices:
            self.aristas[personaje1.nombre][personaje2.nombre] = episodios
            self.aristas[personaje2.nombre][personaje1.nombre] = episodios  # Relación no dirigida

    def obtener_arbol_expansion_minima(self):
        """Uso el algoritmo de Prim para encontrar el árbol de expansión mínima"""
        if not self.vertices:
            return None
        
        import heapq
        
        inicio = list(self.vertices.keys())[0]
        visitados = set([inicio])
        heap = []
        for vecino, peso in self.aristas[inicio].items():
            heapq.heappush(heap, (peso, vecino, inicio))

        arbol_minimo = []

        while heap:
            costo, actual, anterior = heapq.heappop(heap)

            if actual in visitados:
                continue
            
            visitados.add(actual)
            if anterior is not None:
                arbol_minimo.append((anterior, actual, costo))

            for vecino, peso in self.aristas[actual].items():
                if vecino not in visitados:
                    heapq.heappush(heap, (peso, vecino, actual))

        return arbol_minimo

    def contiene_yoda(self, arbol_minimo):
        for anterior, actual, costo in arbol_minimo:
            if actual == "Yoda" or anterior == "Yoda":
                return True
        return False

    def max_episodios_compartidos(self):
        max_episodios = -1
        personajes = ("", "")
        for personaje1 in self.aristas:
            for personaje2, episodios in self.aristas[personaje1].items():
                if episodios > max_episodios:
                    max_episodios = episodios
                    personajes = (personaje1, personaje2)
        return personajes, max_episodios


# Creación del grafo y carga de personajes
grafo = Grafo()

# Carga de personajes
personajes_nombres = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for nombre in personajes_nombres:
    grafo.agregar_personaje(Personaje(nombre))

# Relaciones (episodios compartidos)
grafo.agregar_relacion(grafo.vertices["Luke Skywalker"], grafo.vertices["Darth Vader"], 5)
grafo.agregar_relacion(grafo.vertices["Yoda"], grafo.vertices["Luke Skywalker"], 4)
grafo.agregar_relacion(grafo.vertices["Yoda"], grafo.vertices["Darth Vader"], 2)
grafo.agregar_relacion(grafo.vertices["Yoda"], grafo.vertices["Leia"], 3)  
grafo.agregar_relacion(grafo.vertices["C-3PO"], grafo.vertices["Leia"], 3)
grafo.agregar_relacion(grafo.vertices["Rey"], grafo.vertices["Kylo Ren"], 6)
grafo.agregar_relacion(grafo.vertices["Chewbacca"], grafo.vertices["Han Solo"], 5)
grafo.agregar_relacion(grafo.vertices["R2-D2"], grafo.vertices["Luke Skywalker"], 4)
grafo.agregar_relacion(grafo.vertices["BB-8"], grafo.vertices["Rey"], 2)

# b) Árbol de expansión mínima y determina si contiene a Yoda
arbol_minimo = grafo.obtener_arbol_expansion_minima()
print("Árbol de expansión mínima:")
for anterior, actual, costo in arbol_minimo:
    print(f"{anterior} -- {actual} : {costo}")

contiene_yoda = grafo.contiene_yoda(arbol_minimo)
print(f"¿El árbol de expansión mínima contiene a Yoda? {'Sí' if contiene_yoda else 'No'}")

# c) Número máximo de episodios que comparten dos personajes
personajes, max_episodios = grafo.max_episodios_compartidos()
print(f"Máximo de episodios compartidos: {max_episodios} entre {personajes[0]} y {personajes[1]}.")
