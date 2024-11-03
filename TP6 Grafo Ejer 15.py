class Maravilla:
    def __init__(self, nombre, paises, tipo):
        self.nombre = nombre
        self.paises = paises  # Lista de países
        self.tipo = tipo  # "natural" o "arquitectónica"


class Grafo:
    def __init__(self):
        self.vertices = {}  # Diccionario de maravillas {nombre: Maravilla}
        self.adyacencias = {}  # Diccionario de adyacencias {nombre: {nombre_destino: distancia}}

    def agregar_maravilla(self, maravilla):
        if maravilla.nombre not in self.vertices:
            self.vertices[maravilla.nombre] = maravilla
            self.adyacencias[maravilla.nombre] = {}

    def agregar_arista(self, nombre1, nombre2, distancia):
        if nombre1 in self.vertices and nombre2 in self.vertices:
            self.adyacencias[nombre1][nombre2] = distancia
            self.adyacencias[nombre2][nombre1] = distancia  # Grafo no dirigido


def mst(grafo, tipo):
    import heapq
    visitados = set()
    aristas_mst = []
    distancia_total = 0

    maravillas_tipo = [m for m in grafo.vertices.values() if m.tipo == tipo]
    if not maravillas_tipo:
        return [], 0

    start = maravillas_tipo[0].nombre
    min_heap = [(0, start, start)]  # (distancia, origen, destino)

    while len(visitados) < len(maravillas_tipo):
        distancia, origen, destino = heapq.heappop(min_heap)
        if destino in visitados:
            continue
        visitados.add(destino)
        if origen != destino:
            aristas_mst.append((origen, destino, distancia))
            distancia_total += distancia

        for vecino, dist in grafo.adyacencias[destino].items():
            if vecino not in visitados:
                heapq.heappush(min_heap, (dist, destino, vecino))

    return aristas_mst, distancia_total


def paises_con_ambos_tipos(grafo):
    naturales = set()
    arquitectonicas = set()
    for maravilla in grafo.vertices.values():
        if maravilla.tipo == "natural":
            naturales.update(maravilla.paises)
        elif maravilla.tipo == "arquitectónica":
            arquitectonicas.update(maravilla.paises)
    return naturales.intersection(arquitectonicas)


def paises_con_multiples_maravillas(grafo):
    conteo = {}
    for maravilla in grafo.vertices.values():
        for pais in maravilla.paises:
            if (pais, maravilla.tipo) not in conteo:
                conteo[(pais, maravilla.tipo)] = 0
            conteo[(pais, maravilla.tipo)] += 1
    return {pais_tipo for pais_tipo, cantidad in conteo.items() if cantidad > 1}


# Grafo y agrego maravillas
grafo = Grafo()

# Maravillas arquitectónicas
maravillas_arquitectonicas = [
    Maravilla("Chichén Itzá", ["México"], "arquitectónica"),
    Maravilla("Coliseo de Roma", ["Italia"], "arquitectónica"),
    Maravilla("Cristo Redentor", ["Brasil"], "arquitectónica"),
    Maravilla("Gran Muralla China", ["China"], "arquitectónica"),
    Maravilla("Machu Picchu", ["Perú"], "arquitectónica"),
    Maravilla("Petra", ["Jordania"], "arquitectónica"),
    Maravilla("Taj Mahal", ["India"], "arquitectónica")
]

# Maravillas naturales
maravillas_naturales = [
    Maravilla("Cataratas del Iguazú", ["Argentina", "Brasil"], "natural"),
    Maravilla("Isla de Jeju", ["Corea del Sur"], "natural"),
    Maravilla("Río Subterráneo Puerto Princesa", ["Filipinas"], "natural"),
    Maravilla("Isla de Komodo", ["Indonesia"], "natural"),
    Maravilla("Montaña de la Mesa", ["Sudáfrica"], "natural"),
    Maravilla("Bahía Ha Long", ["Vietnam"], "natural"),
    Maravilla("Amazonia", ["Bolivia", "Brasil", "Colombia", "Ecuador", "Guayana Francesa", "Guyana", "Perú", "Surinam", "Venezuela"], "natural")
]

# Maravillas al grafo
for maravilla in maravillas_arquitectonicas + maravillas_naturales:
    grafo.agregar_maravilla(maravilla)

# Distancias aproximadas (en kilómetros)
distancias = {
    ("Chichén Itzá", "Coliseo de Roma"): 9400,
    ("Chichén Itzá", "Cristo Redentor"): 6600,
    ("Chichén Itzá", "Gran Muralla China"): 12300,
    ("Chichén Itzá", "Machu Picchu"): 4200,
    ("Chichén Itzá", "Petra"): 12300,
    ("Chichén Itzá", "Taj Mahal"): 14600,
    ("Coliseo de Roma", "Cristo Redentor"): 9500,
    ("Coliseo de Roma", "Gran Muralla China"): 7500,
    ("Coliseo de Roma", "Machu Picchu"): 10400,
    ("Coliseo de Roma", "Petra"): 2300,
    ("Coliseo de Roma", "Taj Mahal"): 5800,
    ("Cristo Redentor", "Gran Muralla China"): 17800,
    ("Cristo Redentor", "Machu Picchu"): 3800,
    ("Cristo Redentor", "Petra"): 11200,
    ("Cristo Redentor", "Taj Mahal"): 14500,
    ("Gran Muralla China", "Machu Picchu"): 17400,
    ("Gran Muralla China", "Petra"): 7000,
    ("Gran Muralla China", "Taj Mahal"): 3600,
    ("Machu Picchu", "Petra"): 13400,
    ("Machu Picchu", "Taj Mahal"): 17400,
    ("Petra", "Taj Mahal"): 4100,
    ("Cataratas del Iguazú", "Isla de Jeju"): 18200,
    ("Cataratas del Iguazú", "Río Subterráneo Puerto Princesa"): 19600,
    ("Cataratas del Iguazú", "Isla de Komodo"): 16900,
    ("Cataratas del Iguazú", "Montaña de la Mesa"): 8200,
    ("Cataratas del Iguazú", "Bahía Ha Long"): 18100,
    ("Cataratas del Iguazú", "Amazonia"): 2000,
    ("Isla de Jeju", "Río Subterráneo Puerto Princesa"): 2500,
    ("Isla de Jeju", "Isla de Komodo"): 4700,
    ("Isla de Jeju", "Montaña de la Mesa"): 13200,
    ("Isla de Jeju", "Bahía Ha Long"): 3000,
    ("Isla de Jeju", "Amazonia"): 17200,
    ("Río Subterráneo Puerto Princesa", "Isla de Komodo"): 2100,
    ("Río Subterráneo Puerto Princesa", "Montaña de la Mesa"): 11500,
    ("Río Subterráneo Puerto Princesa", "Bahía Ha Long"): 1600,
    ("Río Subterráneo Puerto Princesa", "Amazonia"): 18600,
    ("Isla de Komodo", "Montaña de la Mesa"): 9900,
    ("Isla de Komodo", "Bahía Ha Long"): 4400,
    ("Isla de Komodo", "Amazonia"): 16500,
    ("Montaña de la Mesa", "Bahía Ha Long"): 11500,
    ("Montaña de la Mesa", "Amazonia"): 12000,
    ("Bahía Ha Long", "Amazonia"): 17500,
}

# Aristas al grafo
for (origen, destino), distancia in distancias.items():
    grafo.agregar_arista(origen, destino, distancia)

# Árbol de expansión mínimo y otras consultas
mst_arquitectonicas, distancia_total_arquitectonicas = mst(grafo, "arquitectónica")
mst_naturales, distancia_total_naturales = mst(grafo, "natural")
paises_ambos_tipos = paises_con_ambos_tipos(grafo)
paises_multiples = paises_con_multiples_maravillas(grafo)

# Salidas
print("Árbol de expansión mínimo (arquitectónicas):", mst_arquitectonicas)
print("Distancia total (arquitectónicas):", distancia_total_arquitectonicas)
print("Árbol de expansión mínimo (naturales):", mst_naturales)
print("Distancia total (naturales):", distancia_total_naturales)
print("Países con maravillas de ambos tipos:", paises_ambos_tipos)
print("Países con múltiples maravillas del mismo tipo:", paises_multiples)
