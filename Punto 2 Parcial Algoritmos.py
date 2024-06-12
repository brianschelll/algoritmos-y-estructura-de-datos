class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamano(self):
        return len(self.items)

# Datos de dinosaurios
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },
]

def contar_especies(pila):
    especies = set()
    pila_aux = Pila()
    while not pila.esta_vacia():
        dinosaurio = pila.desapilar()
        especies.add(dinosaurio['especie'])
        pila_aux.apilar(dinosaurio)
    
    # Restaurar la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return len(especies)

def contar_descubridores(pila):
    descubridores = set()
    pila_aux = Pila()
    while not pila.esta_vacia():
        dinosaurio = pila.desapilar()
        descubridores.add(dinosaurio['descubridor'])
        pila_aux.apilar(dinosaurio)
    
    # Restaurar la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return len(descubridores)

def mostrar_nombres_dinosaurios_con_t(pila):
    pila_aux = Pila()
    resultado = []
    while not pila.esta_vacia():
        dinosaurio = pila.desapilar()
        if dinosaurio['nombre'].startswith('T'):
            resultado.append(dinosaurio['nombre'])
        pila_aux.apilar(dinosaurio)
    
    # Restaurar la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return resultado

def mostrar_nombres_dinosaurios_peso_menor(pila, peso_limite):
    pila_aux = Pila()
    resultado = []
    while not pila.esta_vacia():
        dinosaurio = pila.desapilar()
        peso_kg = int(dinosaurio['peso'].split()[0])
        if peso_kg < peso_limite:
            resultado.append(dinosaurio['nombre'])
        pila_aux.apilar(dinosaurio)
    
    # Restaurar la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return resultado

def separar_nombres_dinosaurios_por_letra(pila, letras):
    pila_aux = Pila()
    pila_separada = Pila()
    while not pila.esta_vacia():
        dinosaurio = pila.desapilar()
        if dinosaurio['nombre'][0] in letras:
            pila_separada.apilar(dinosaurio['nombre'])
        else:
            pila_aux.apilar(dinosaurio)
    
    # Restaurar la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return pila_separada

# Crear la pila de dinosaurios
pila_dinosaurios = Pila()
for dino in dinosaurios:
    pila_dinosaurios.apilar(dino)

# Ejecución de las actividades
print("Número de especies:", contar_especies(pila_dinosaurios))
print("Número de descubridores:", contar_descubridores(pila_dinosaurios))

print("Dinosaurios que empiezan con 'T':")
for nombre in mostrar_nombres_dinosaurios_con_t(pila_dinosaurios):
    print(nombre)

print("Dinosaurios que pesan menos de 275 Kg:")
for nombre in mostrar_nombres_dinosaurios_peso_menor(pila_dinosaurios, 275):
    print(nombre)

pila_separada = separar_nombres_dinosaurios_por_letra(pila_dinosaurios, {'A', 'Q', 'S'})
print("Dinosaurios en la pila separada (A, Q, S):")
while not pila_separada.esta_vacia():
    print(pila_separada.desapilar())