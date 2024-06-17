# Definición de datos de entrenadores y pokemones
entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120,
        "pokemones": [
            {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
        ]
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "pokemones": [
            {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico"},
        ]
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100,
        "pokemones": [
            {"nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None},
            {"nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
        ]
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30,
        "pokemones": [
            {"nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra"},
            {"nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra"},
        ]
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60,
        "pokemones": [
            {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None},
            {"nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None},
        ]
    }
]

def cantidad_pokemons(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador["nombre"] == entrenador_nombre:
            return len(entrenador["pokemones"])
    return 0

def entrenadores_mas_de_tres_torneos():
    return [entrenador["nombre"] for entrenador in entrenadores if entrenador["torneos_ganados"] > 3]

def pokemon_mayor_nivel_entrenador_top():
    top_entrenador = max(entrenadores, key=lambda x: x["torneos_ganados"])
    pokemon_top = max(top_entrenador["pokemones"], key=lambda x: x["nivel"])
    return pokemon_top

def mostrar_datos_entrenador(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador["nombre"] == entrenador_nombre:
            return entrenador
    return None

def entrenadores_mayor_79_ganadas():
    return [
        entrenador["nombre"] 
        for entrenador in entrenadores 
        if entrenador["batallas_ganadas"] / (entrenador["batallas_ganadas"] + entrenador["batallas_perdidas"]) > 0.79
    ]

def entrenadores_tipo_fuego_planta_agua_volador():
    return [
        entrenador["nombre"] 
        for entrenador in entrenadores 
        if any(pokemon["tipo"] == "Fuego" or pokemon["tipo"] == "Planta" for pokemon in entrenador["pokemones"]) and 
           any(pokemon["tipo"] == "Agua" and pokemon["subtipo"] == "Volador" for pokemon in entrenador["pokemones"])
    ]

def promedio_nivel_pokemons(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador["nombre"] == entrenador_nombre:
            niveles = [pokemon["nivel"] for pokemon in entrenador["pokemones"]]
            return sum(niveles) / len(niveles) if niveles else 0
    return 0

def entrenadores_con_pokemon(pokemon_nombre):
    return [entrenador["nombre"] for entrenador in entrenadores if any(pokemon["nombre"] == pokemon_nombre for pokemon in entrenador["pokemones"])]

def entrenadores_con_pokemons_repetidos():
    return [
        entrenador["nombre"] 
        for entrenador in entrenadores 
        if len(entrenador["pokemones"]) != len(set(pokemon["nombre"] for pokemon in entrenador["pokemones"]))
    ]

def entrenadores_con_pokemons_especificos():
    pokemons_especificos = {"Tyrantrum", "Terrakion", "Wingull"}
    return [
        entrenador["nombre"] 
        for entrenador in entrenadores 
        if any(pokemon["nombre"] in pokemons_especificos for pokemon in entrenador["pokemones"])
    ]

def entrenador_tiene_pokemon(entrenador_nombre, pokemon_nombre):
    for entrenador in entrenadores:
        if entrenador["nombre"] == entrenador_nombre:
            for pokemon in entrenador["pokemones"]:
                if pokemon["nombre"] == pokemon_nombre:
                    return entrenador, pokemon
    return None, None


#a 
print('A cantidad de pokemones:')
print(cantidad_pokemons("Ash Ketchum"))
#b
print('B cantidad de entrenadores con mas de 3 torneos ganados: ')
print(entrenadores_mas_de_tres_torneos())
#c
print('C Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados:')
print(pokemon_mayor_nivel_entrenador_top())
#d
print('D Datos de entrenador:')
print(mostrar_datos_entrenador("Leon"))
#E
print('E Entrenadore con mas del 79 porciento de batallas ganadas:')
print(entrenadores_mayor_79_ganadas())
#f 
print('F entrenadores que tengan Pokémons de tipo fuego y planta agua o volador:')
print(entrenadores_tipo_fuego_planta_agua_volador())
#g
print('G romedio de nivel de los Pokémons de un determinado entrenador:')
print(promedio_nivel_pokemons("Goh"))
#h
print('H determinar cuántos entrenadores tienen a un determinado Pokémon:')
print(entrenadores_con_pokemon("Pikachu"))
#i
print('I mostrar los entrenadores que tienen Pokémons repetidos:')
print(entrenadores_con_pokemons_repetidos())
#j
print('J determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull')
print(entrenadores_con_pokemons_especificos())
#k
print('K Determinar si un entrenador “X” tiene al Pokémon “Y”:')
entrenador, pokemon = entrenador_tiene_pokemon("Ash Ketchum", "Pikachu")
if entrenador and pokemon:
    print(entrenador)
    print(pokemon)

