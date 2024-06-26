class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
    
    def funcion_hash(self, clave):
        return clave % self.tamaño
    
    def insertar(self, clave, valor):
        hash_clave = self.funcion_hash(clave)
        self.tabla[hash_clave].append(valor)
    
    def buscar(self, clave):
        hash_clave = self.funcion_hash(clave)
        return self.tabla[hash_clave]

pokemons = [
    {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
    {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
    {"nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico"},
    {"nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None},
    {"nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
    {"nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None},
    {"nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None},
    {"nombre": "Umbreon", "nivel": 45, "tipo": "Siniestro", "subtipo": None},
    {"nombre": "Nidoking", "nivel": 40, "tipo": "Veneno", "subtipo": "Tierra"},
]

# tablas hash
tabla_hash_tipo = TablaHash(10)
tabla_hash_ultimo_digito = TablaHash(10)
tabla_hash_nivel = TablaHash(10)

# los Pokemon en las tablas hash
for pokemon in pokemons:
    # Primera tabla hash (tipo)
    tabla_hash_tipo.insertar(hash(pokemon["tipo"]), pokemon)
    if pokemon["subtipo"]:
        tabla_hash_tipo.insertar(hash(pokemon["subtipo"]), pokemon)
    
    # Segunda tabla hash (último dígito del nivel)
    ultimo_digito = pokemon["nivel"] % 10
    tabla_hash_ultimo_digito.insertar(ultimo_digito, pokemon)
    
    # Tercera tabla hash (nivel)
    nivel_clave = pokemon["nivel"] // 10
    tabla_hash_nivel.insertar(nivel_clave, pokemon)

#  Pokemon cuyos números terminan en 3, 7 y 9
print("Pokémon cuyos niveles terminan en 3, 7 y 9:")
for digito in [3, 7, 9]:
    for pokemon in tabla_hash_ultimo_digito.buscar(digito):
        print(pokemon)

#  Pokemon cuyos niveles son múltiplos de 2, 5 y 10
print("\nPokémon cuyos niveles son múltiplos de 2, 5 y 10:")
for clave in range(0, 5):
    for pokemon in tabla_hash_nivel.buscar(clave):
        if pokemon["nivel"] % 2 == 0 or pokemon["nivel"] % 5 == 0:
            print(pokemon)

# Pokemon de los siguientes tipos: Acero, Fuego, Eléctrico, Hielo
tipos_interes = ["Acero", "Fuego", "Eléctrico", "Hielo"]
print("\nPokémon de tipos Acero, Fuego, Eléctrico, Hielo:")
for tipo in tipos_interes:
    for pokemon in tabla_hash_tipo.buscar(hash(tipo)):
        print(pokemon)

