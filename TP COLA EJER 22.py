class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, personaje):
        self.cola.append(personaje)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.cola) == 0

    def frente(self):
        if not self.esta_vacia():
            return self.cola[0]
        else:
            return None

    def tamano(self):
        return len(self.cola)
    
    def recorrer(self):
        for personaje in self.cola:
            print(personaje)

# Definición de la cola de personajes del MCU
cola_personajes = Cola()

# Personajes conocidos
personajes = [
    {"nombre_personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre_personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"nombre_personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre_personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre_personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"}
]

# Encolar personajes
for personaje in personajes:
    cola_personajes.encolar(personaje)

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def obtener_personaje_capitana_marvel(cola):
    for personaje in cola.cola:
        if personaje["superheroe"] == "Capitana Marvel":
            return personaje["nombre_personaje"]
    return "Capitana Marvel no está en la cola."

# b. Mostrar los nombres de los superhéroes femeninos
def superheroes_femeninos(cola):
    femeninos = [personaje["superheroe"] for personaje in cola.cola if personaje["genero"] == "F"]
    return femeninos

# c. Mostrar los nombres de los personajes masculinos
def personajes_masculinos(cola):
    masculinos = [personaje["nombre_personaje"] for personaje in cola.cola if personaje["genero"] == "M"]
    return masculinos

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def superheroe_scott_lang(cola):
    for personaje in cola.cola:
        if personaje["nombre_personaje"] == "Scott Lang":
            return personaje["superheroe"]
    return "Scott Lang no está en la cola."

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra 'S'
def personajes_con_s(cola):
    con_s = [personaje for personaje in cola.cola if personaje["nombre_personaje"].startswith('S') or personaje["superheroe"].startswith('S')]
    return con_s

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
def personaje_carol_danvers(cola):
    for personaje in cola.cola:
        if personaje["nombre_personaje"] == "Carol Danvers":
            return personaje["superheroe"]
    return "Carol Danvers no está en la cola."
    
# Ejecución de las actividades
print("a. Nombre del personaje de Capitana Marvel:", obtener_personaje_capitana_marvel(cola_personajes))
print("b. Superhéroes femeninos:", superheroes_femeninos(cola_personajes))
print("c. Personajes masculinos:", personajes_masculinos(cola_personajes))
print("d. Superhéroe de Scott Lang:", superheroe_scott_lang(cola_personajes))
print("e. Personajes o superhéroes cuyos nombres comienzan con 'S':", personajes_con_s(cola_personajes))
print("f. Superhéroe de Carol Danvers:", personaje_carol_danvers(cola_personajes))
