class NodoCriatura:
    def __init__(self, nombre, derrotado_por=None, capturada_por=None, descripcion=""):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.capturada_por = capturada_por
        self.descripcion = descripcion
        self.izquierda = None
        self.derecha = None

class ArbolCriaturas:
    def __init__(self):
        self.raiz = None

    # a. Listado inorden de las criaturas y quienes las derrotaron
    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}")
            self.inorden(nodo.derecha)

    # Insertar criaturas
    def insertar(self, nombre, derrotado_por=None, capturada_por=None, descripcion=""):
        nuevo_nodo = NodoCriatura(nombre, derrotado_por, capturada_por, descripcion)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecha, nuevo_nodo)
        
    # b. Cargar descripción de una criatura
    def cargar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.descripcion = descripcion
            print(f"Descripción de {nombre} actualizada.")
        else:
            print(f"Criatura {nombre} no encontrada.")

    # c. Mostrar toda la información de la criatura Talos
    def mostrar_informacion(self, nombre):
        nodo = self.buscar(nombre)
        if nodo:
            print(f"Criatura: {nodo.nombre}")
            print(f"Derrotado por: {nodo.derrotado_por}")
            print(f"Capturada por: {nodo.capturada_por}")
            print(f"Descripción: {nodo.descripcion}")
        else:
            print(f"Criatura {nombre} no encontrada.")

    # d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
    def top_3_heroes(self):
        derrotas = {}
        self._contar_derrotas(self.raiz, derrotas)
        top_3 = sorted(derrotas.items(), key=lambda x: x[1], reverse=True)[:3]
        print(" d. Top 3 héroes o dioses que derrotaron más criaturas:")
        for heroe, cantidad in top_3:
            print(f"{heroe}: {cantidad} criaturas")

    def _contar_derrotas(self, nodo, derrotas):
        if nodo:
            if nodo.derrotado_por:
                if nodo.derrotado_por in derrotas:
                    derrotas[nodo.derrotado_por] += 1
                else:
                    derrotas[nodo.derrotado_por] = 1
            self._contar_derrotas(nodo.izquierda, derrotas)
            self._contar_derrotas(nodo.derecha, derrotas)

    # e. Listar criaturas derrotadas por Heracles
    def listar_derrotadas_por(self, heroe):
        print(f"Criaturas derrotadas por {heroe}:")
        self._listar_por_heroe(self.raiz, heroe)

    def _listar_por_heroe(self, nodo, heroe):
        if nodo:
            if nodo.derrotado_por == heroe:
                print(nodo.nombre)
            self._listar_por_heroe(nodo.izquierda, heroe)
            self._listar_por_heroe(nodo.derecha, heroe)

    # f. Listar criaturas que no han sido derrotadas
    def listar_no_derrotadas(self):
        print("Criaturas que no han sido derrotadas:")
        self._listar_no_derrotadas(self.raiz)

    def _listar_no_derrotadas(self, nodo):
        if nodo:
            if nodo.derrotado_por is None:
                print(nodo.nombre)
            self._listar_no_derrotadas(nodo.izquierda)
            self._listar_no_derrotadas(nodo.derecha)

    # g. Campo “capturada” que almacenará el nombre del héroe o dios que la capturó
    def capturar_criatura(self, nombre, capturada_por):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.capturada_por = capturada_por
            print(f"{nombre} capturada por {capturada_por}.")
        else:
            print(f"Criatura {nombre} no encontrada.")

    # h. Modificar nodos de Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó
    def modificar_capturadas_por_heracles(self):
        criaturas = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
        for criatura in criaturas:
            self.capturar_criatura(criatura, "Heracles")

    # i. Búsquedas por coincidencia
    def buscar_por_coincidencia(self, termino):
        print(f"Resultados de búsqueda para '{termino}':")
        self._buscar_coincidencia(self.raiz, termino)

    def _buscar_coincidencia(self, nodo, termino):
        if nodo:
            if termino.lower() in nodo.nombre.lower():
                print(nodo.nombre)
            self._buscar_coincidencia(nodo.izquierda, termino)
            self._buscar_coincidencia(nodo.derecha, termino)

    # j. Eliminar al Basilisco y a las Sirenas
    def eliminar_criatura(self, nombre):
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self, nodo, nombre):
        if not nodo:
            return nodo
        if nombre < nodo.nombre:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nombre)
        else:
            # Nodo encontrado
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            temp = self._minimo(nodo.derecha)
            nodo.nombre = temp.nombre
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.nombre)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    # k. Modificar nodo de las Aves del Estínfalo agregando que Heracles derrotó a varias
    def modificar_aves_estinfalo(self):
        nodo = self.buscar("Aves del Estínfalo")
        if nodo:
            nodo.derrotado_por = "Heracles"
            print(f"Modificado: {nodo.nombre} derrotado por Heracles.")

    # l. Modificar el nombre de la criatura Ladón por Dragón Ladón
    def modificar_nombre_ladon(self):
        nodo = self.buscar("Ladón")
        if nodo:
            nodo.nombre = "Dragón Ladón"
            print("Nombre de Ladón modificado a Dragón Ladón.")
        else:
            print("Ladón no encontrado.")

    # m. Listado por nivel del árbol
    def listado_por_nivel(self):
        if not self.raiz:
            return
        print("Listado por niveles:")
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            print(f"Criatura: {actual.nombre}, Derrotado por: {actual.derrotado_por}, Capturada por: {actual.capturada_por}")
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)

    # n. Mostrar criaturas capturadas por Heracles
    def mostrar_capturadas_por(self, capturador):
        print(f"Criaturas capturadas por {capturador}:")
        self._mostrar_capturadas_por(self.raiz, capturador)

    def _mostrar_capturadas_por(self, nodo, capturador):
        if nodo:
            if nodo.capturada_por == capturador:
                print(nodo.nombre)
            self._mostrar_capturadas_por(nodo.izquierda, capturador)
            self._mostrar_capturadas_por(nodo.derecha, capturador)

    # Buscar nodo por nombre
    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if not nodo or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        return self._buscar_recursivo(nodo.derecha, nombre)

# Crear el árbol y poblarlo con datos iniciales
arbol = ArbolCriaturas()

# Poblamos el árbol con las criaturas y sus derrotados
datos_criaturas = [
    ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"), ("Dino", None), 
    ("Pefredo", None), ("Enio", None), ("Escila", None), ("Caribdis", None), 
    ("Euríale", None), ("Esteno", None), ("Medusa", "Perseo"), ("Ladón", "Heracles"), 
    ("Águila del Cáucaso", None), ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"), 
    ("León de Nemea", "Heracles"), ("Esfinge", "Edipo"), ("Dragón de la Cólquida", None), 
    ("Cerbero", None), ("Toro de Creta", "Teseo"), ("Jabalí de Erimanto", None),
    ("Minotauro de Creta", "Teseo"), ("Talos", "Medea"), ("Aves del Estínfalo", None), 
    ("Basilisco", None), ("Sirenas", None)
]

for criatura, derrotado_por in datos_criaturas:
    arbol.insertar(criatura, derrotado_por)

# Ejemplo de uso:
arbol.inorden(arbol.raiz)
arbol.cargar_descripcion("Tifón", "Monstruo gigante con cientos de cabezas de dragón.")
arbol.mostrar_informacion("Talos")
arbol.top_3_heroes()
arbol.listar_derrotadas_por("Heracles")
arbol.listar_no_derrotadas()
arbol.modificar_capturadas_por_heracles()
arbol.buscar_por_coincidencia("Cerbero")
arbol.eliminar_criatura("Basilisco")
arbol.eliminar_criatura("Sirenas")
arbol.modificar_aves_estinfalo()
arbol.modificar_nombre_ladon()
arbol.listado_por_nivel()
arbol.mostrar_capturadas_por("Heracles")
