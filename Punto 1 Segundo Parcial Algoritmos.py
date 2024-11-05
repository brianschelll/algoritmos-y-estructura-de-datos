class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos  # Lista de tipos 

class Nodo:
    def __init__(self, data):
        self.data = data
        self.pokemones = [data]  # Lista de Pokémon con el mismo tipo 
        self.left = None
        self.right = None

class ArbolBinarioBusqueda:
    def __init__(self, indice):
        self.root = None
        self.indice = indice  # Índice para ordenar: 'nombre', 'numero' o 'tipos'

    def _insertar_rec(self, nodo, data):
        key = getattr(data, self.indice)
        node_key = getattr(nodo.data, self.indice)

        if key == node_key:
            nodo.pokemones.append(data)  # Agrega el Pokémon a la lista en el nodo existente
        elif key < node_key:
            if nodo.left is None:
                nodo.left = Nodo(data)
            else:
                self._insertar_rec(nodo.left, data)
        else:
            if nodo.right is None:
                nodo.right = Nodo(data)
            else:
                self._insertar_rec(nodo.right, data)

    def insertar(self, data):
        if self.root is None:
            self.root = Nodo(data)
        else:
            self._insertar_rec(self.root, data)

    def _buscar_proximidad(self, nodo, substring, resultados):
        if nodo is not None:
            for pokemon in nodo.pokemones:
                if substring.lower() in pokemon.nombre.lower():
                    resultados.append(pokemon)
            self._buscar_proximidad(nodo.left, substring, resultados)
            self._buscar_proximidad(nodo.right, substring, resultados)

    def buscar_por_proximidad(self, substring):
        resultados = []
        self._buscar_proximidad(self.root, substring, resultados)
        return resultados

    def _listar_por_tipo(self, nodo, tipo, resultados):
        if nodo is not None:
            if tipo in getattr(nodo.data, 'tipos'):
                for pokemon in nodo.pokemones:
                    if pokemon.nombre not in resultados:  # Evita duplicados
                        resultados.append(pokemon.nombre)
            self._listar_por_tipo(nodo.left, tipo, resultados)
            self._listar_por_tipo(nodo.right, tipo, resultados)

    def listar_por_tipo(self, tipo):
        resultados = []
        self._listar_por_tipo(self.root, tipo, resultados)
        return resultados

    def _listado_ordenado(self, nodo, resultados):
        if nodo is not None:
            self._listado_ordenado(nodo.left, resultados)
            for pokemon in nodo.pokemones:
                resultados.append((pokemon.numero, pokemon.nombre))
            self._listado_ordenado(nodo.right, resultados)

    def listado_ordenado(self):
        resultados = []
        self._listado_ordenado(self.root, resultados)
        return resultados

    def listado_por_nivel(self):
        if not self.root:
            return []
        queue = [self.root]
        resultados = []
        while queue:
            nodo = queue.pop(0)
            for pokemon in nodo.pokemones:
                resultados.append(pokemon.nombre)
            if nodo.left:
                queue.append(nodo.left)
            if nodo.right:
                queue.append(nodo.right)
        return resultados

    def _contar_por_tipo(self, nodo, tipo):
        if nodo is None:
            return 0
        contador = sum(1 for pokemon in nodo.pokemones if tipo in pokemon.tipos)
        contador += self._contar_por_tipo(nodo.left, tipo)
        contador += self._contar_por_tipo(nodo.right, tipo)
        return contador

    def contar_por_tipo(self, tipo):
        return self._contar_por_tipo(self.root, tipo)

    def buscar_por_numero(self, numero):
        actual = self.root
        while actual is not None:
            if actual.data.numero == numero:
                return actual.data
            elif numero < actual.data.numero:
                actual = actual.left
            else:
                actual = actual.right
        return None

# Creación de los tres árboles binarios de búsqueda
arbol_nombre = ArbolBinarioBusqueda('nombre')
arbol_numero = ArbolBinarioBusqueda('numero')
arbol_tipo = ArbolBinarioBusqueda('tipos')

# Carga de pokémones
pokemones = [
    Pokemon("Jolteon", 135, ["eléctrico"]),           
    Pokemon("Lycanroc", 745, ["roca"]),               
    Pokemon("Tyrantrum", 697, ["roca", "dragón"]),   
    Pokemon("Bulbasaur", 1, ["planta", "veneno"]),    
    Pokemon("Chikorita", 152, ["planta"]),            
    Pokemon("Treecko", 252, ["planta"]),              
    Pokemon("Turtwig", 387, ["planta"]),              
    Pokemon("Snivy", 495, ["planta"]),                
    Pokemon("Froakie", 656, ["agua"]),                
    Pokemon("Rowlet", 722, ["planta", "volador"]),   
    Pokemon("Cinderace", 815, ["fuego"]),             
]

for pokemon in pokemones:
    arbol_nombre.insertar(pokemon)
    arbol_numero.insertar(pokemon)
    for tipo in pokemon.tipos:  # Asegura que cada tipo esté registrado por separado
        arbol_tipo.insertar(pokemon)

# b) Búsqueda por número y por proximidad en el nombre
pokemon_buscado = arbol_numero.buscar_por_numero(152)  
if pokemon_buscado:
    print(f"Búsqueda por número: {pokemon_buscado.nombre} - Número: {pokemon_buscado.numero} - Tipos: {pokemon_buscado.tipos}")
else:
    print("No se encontró Pokémon con ese número.")

resultados_proximidad = arbol_nombre.buscar_por_proximidad("bul")
print("Búsqueda por proximidad ('bul'):")
for pokemon in resultados_proximidad:
    print(f"{pokemon.nombre} - Número: {pokemon.numero} - Tipos: {pokemon.tipos}")

# c) Mostrar nombres de todos los Pokémon de determinados tipos
for tipo in ["agua", "fuego", "planta", "eléctrico"]:
    print(f"Pokémon de tipo {tipo}: {arbol_tipo.listar_por_tipo(tipo)}")

# d) Listado ascendente por número y nombre, y listado por nivel por nombre
print("Listado ascendente por número y nombre:")
for numero, nombre in arbol_numero.listado_ordenado():
    print(f"{numero} - {nombre}")

print("Listado por nivel (nombre):", arbol_nombre.listado_por_nivel())

# e) Mostrar datos de Pokémon específicos
especificos = ["Jolteon", "Lycanroc", "Tyrantrum"]
print("Datos de Pokémon específicos:")
for nombre in especificos:
    resultados = arbol_nombre.buscar_por_proximidad(nombre)
    for pokemon in resultados:
        print(f"{pokemon.nombre} - Número: {pokemon.numero} - Tipos: {pokemon.tipos}")

# f) Contar Pokémon de tipo eléctrico y acero
print("Cantidad de Pokémon de tipo eléctrico:", arbol_tipo.contar_por_tipo("eléctrico"))
print("Cantidad de Pokémon de tipo acero:", arbol_tipo.contar_por_tipo("acero"))

