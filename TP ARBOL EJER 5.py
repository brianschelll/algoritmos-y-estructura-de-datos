class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True para héroes, False para villanos
        self.izquierda = None
        self.derecha = None

class ArbolMCU:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        if self.raiz is None:
            self.raiz = NodoArbol(nombre, es_heroe)
        else:
            self._insertar_rec(self.raiz, nombre, es_heroe)

    def _insertar_rec(self, nodo, nombre, es_heroe):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(nombre, es_heroe)
            else:
                self._insertar_rec(nodo.izquierda, nombre, es_heroe)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(nombre, es_heroe)
            else:
                self._insertar_rec(nodo.derecha, nombre, es_heroe)

    def inorden(self, nodo, lista):
        """Recorrido en inorden (ascendente)"""
        if nodo is not None:
            self.inorden(nodo.izquierda, lista)
            lista.append(nodo)
            self.inorden(nodo.derecha, lista)

    def contar_superheroes(self, nodo):
        """Cuenta la cantidad de héroes (es_heroe = True) en el árbol"""
        if nodo is None:
            return 0
        cuenta_izquierda = self.contar_superheroes(nodo.izquierda)
        cuenta_derecha = self.contar_superheroes(nodo.derecha)
        return cuenta_izquierda + cuenta_derecha + (1 if nodo.es_heroe else 0)

    def buscar_proximidad(self, nodo, nombre):
        """Búsqueda por proximidad (nombre parcial o aproximado)"""
        if nodo is None:
            return None
        if nombre.lower() in nodo.nombre.lower():
            return nodo
        if nombre < nodo.nombre:
            return self.buscar_proximidad(nodo.izquierda, nombre)
        else:
            return self.buscar_proximidad(nodo.derecha, nombre)

    def listar_superheroes_con_c(self, nodo, lista):
        """Lista los superhéroes cuyos nombres empiezan con 'C'"""
        if nodo is not None:
            self.listar_superheroes_con_c(nodo.izquierda, lista)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                lista.append(nodo.nombre)
            self.listar_superheroes_con_c(nodo.derecha, lista)

    def separar_en_bosques(self):
        """Genera dos árboles separados: uno de héroes y otro de villanos"""
        arbol_heroes = ArbolMCU()
        arbol_villanos = ArbolMCU()
        self._separar_rec(self.raiz, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def _separar_rec(self, nodo, arbol_heroes, arbol_villanos):
        if nodo is not None:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, True)
            else:
                arbol_villanos.insertar(nodo.nombre, False)
            self._separar_rec(nodo.izquierda, arbol_heroes, arbol_villanos)
            self._separar_rec(nodo.derecha, arbol_heroes, arbol_villanos)

# Crear el árbol con personajes de MCU
arbol_mcu = ArbolMCU()

# Insertar personajes (True = Héroe, False = Villano)
personajes = [
    ("Iron Man", True), ("Thanos", False), ("Captain America", True),
    ("Black Widow", True), ("Loki", False), ("Thor", True),
    ("Hela", False), ("Doctor Strange", True), ("Ultron", False),
    ("Wanda Maximoff", True), ("Vision", True), ("Green Goblin", False)
]

for nombre, es_heroe in personajes:
    arbol_mcu.insertar(nombre, es_heroe)

# a. Además del nombre del superhéroe, en cada nodo del árbol se almacena un campo booleano
#    que indica si es un héroe (True) o un villano (False).
# Ya está implementado en la clase NodoArbol

# b. Listar los villanos ordenados alfabéticamente
def listar_villanos(arbol):
    villanos = []
    arbol.inorden(arbol.raiz, villanos)
    villanos = [nodo.nombre for nodo in villanos if not nodo.es_heroe]
    print("Villanos en orden alfabético:", villanos)

listar_villanos(arbol_mcu)

# c. Mostrar todos los superhéroes que empiezan con C
def listar_superheroes_con_C(arbol):
    lista_heroes_C = []
    arbol.listar_superheroes_con_c(arbol.raiz, lista_heroes_C)
    print("Superhéroes que empiezan con 'C':", lista_heroes_C)

listar_superheroes_con_C(arbol_mcu)

# d. Determinar cuántos superhéroes hay en el árbol
def contar_superheroes(arbol):
    cantidad_heroes = arbol.contar_superheroes(arbol.raiz)
    print("Cantidad de superhéroes en el árbol:", cantidad_heroes)

contar_superheroes(arbol_mcu)

# e. Doctor Strange está mal cargado, utilizar búsqueda por proximidad para corregir
def corregir_nombre(arbol, nombre_incorrecto, nuevo_nombre):
    nodo = arbol.buscar_proximidad(arbol.raiz, nombre_incorrecto)
    if nodo:
        print(f"Corrigiendo nombre: {nodo.nombre} a {nuevo_nombre}")
        nodo.nombre = nuevo_nombre
    else:
        print(f"No se encontró un personaje cercano a {nombre_incorrecto}")

corregir_nombre(arbol_mcu, "Doctor", "Doctor Strange")

# f. Listar los superhéroes ordenados de manera descendente
def listar_superheroes_descendente(arbol):
    lista_heroes = []
    arbol.inorden(arbol.raiz, lista_heroes)
    heroes_descendente = [nodo.nombre for nodo in lista_heroes if nodo.es_heroe]
    heroes_descendente.sort(reverse=True)
    print("Superhéroes en orden descendente:", heroes_descendente)

listar_superheroes_descendente(arbol_mcu)

# g. Generar un bosque de superhéroes y villanos
arbol_heroes, arbol_villanos = arbol_mcu.separar_en_bosques()

# I. Determinar cuántos nodos tiene cada árbol
def contar_nodos(arbol):
    return arbol.contar_superheroes(arbol.raiz) if arbol else 0

print("Cantidad de nodos en el árbol de héroes:", contar_nodos(arbol_heroes))
print("Cantidad de nodos en el árbol de villanos:", contar_nodos(arbol_villanos))

# II. Barrido ordenado alfabéticamente de cada árbol
def barrido_ordenado(arbol, descripcion):
    lista = []
    arbol.inorden(arbol.raiz, lista)
    nombres = [nodo.nombre for nodo in lista]
    print(f"{descripcion} en orden alfabético:", nombres)

barrido_ordenado(arbol_heroes, "Héroes")
barrido_ordenado(arbol_villanos, "Villanos")
