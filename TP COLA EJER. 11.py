class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.frente = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo

    def desencolar(self):
        if not self.esta_vacia():
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return dato
        else:
            return None

    def ver_frente(self):
        if not self.esta_vacia():
            return self.frente.dato
        else:
            return None

    def recorrer(self):
        actual = self.frente
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

    def insertar_antes_de(self, nombre, nuevo_personaje):
        """Inserta un nuevo personaje antes del personaje con el nombre dado"""
        if self.esta_vacia():
            return

        nuevo_nodo = Nodo(nuevo_personaje)
        actual = self.frente
        anterior = None

        while actual is not None and actual.dato["nombre"] != nombre:
            anterior = actual
            actual = actual.siguiente

        if actual is not None:
            if anterior is None:
                # Insertar al principio de la cola
                nuevo_nodo.siguiente = self.frente
                self.frente = nuevo_nodo
            else:
                # Insertar en el medio
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = actual

    def eliminar_despues_de(self, nombre):
        """Elimina el personaje que está ubicado después del personaje con el nombre dado"""
        if self.esta_vacia():
            return

        actual = self.frente

        while actual is not None and actual.dato["nombre"] != nombre:
            actual = actual.siguiente

        if actual is not None and actual.siguiente is not None:
            actual.siguiente = actual.siguiente.siguiente
            if actual.siguiente is None:
                self.final = actual

# Crear la cola de personajes
cola_personajes = Cola()

# Encolar algunos personajes de Star Wars
cola_personajes.encolar({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
cola_personajes.encolar({"nombre": "Leia Organa", "planeta": "Alderaan"})
cola_personajes.encolar({"nombre": "Han Solo", "planeta": "Corellia"})
cola_personajes.encolar({"nombre": "Yoda", "planeta": "Dagobah"})
cola_personajes.encolar({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
cola_personajes.encolar({"nombre": "Chewbacca", "planeta": "Kashyyyk"})
cola_personajes.encolar({"nombre": "Wicket", "planeta": "Endor"})

# a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
def mostrar_personajes_por_planeta(cola, planetas):
    actual = cola.frente
    print("Personajes de los planetas seleccionados:")
    while actual is not None:
        if actual.dato["planeta"] in planetas:
            print(f'{actual.dato["nombre"]} es de {actual.dato["planeta"]}')
        actual = actual.siguiente

# Planetas a mostrar
planetas_seleccionados = ["Alderaan", "Endor", "Tatooine"]
mostrar_personajes_por_planeta(cola_personajes, planetas_seleccionados)

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
def indicar_planeta_natal(cola, nombres):
    actual = cola.frente
    print("Planetas natales de personajes seleccionados:")
    while actual is not None:
        if actual.dato["nombre"] in nombres:
            print(f'{actual.dato["nombre"]} es de {actual.dato["planeta"]}')
        actual = actual.siguiente

# Personajes a buscar
personajes_a_buscar = ["Luke Skywalker", "Han Solo"]
indicar_planeta_natal(cola_personajes, personajes_a_buscar)

# c. Insertar un nuevo personaje antes del maestro Yoda
nuevo_personaje = {"nombre": "Ahsoka Tano", "planeta": "Shili"}
cola_personajes.insertar_antes_de("Yoda", nuevo_personaje)

# Recorrer la cola después de la inserción
print("\nCola después de insertar antes de Yoda:")
cola_personajes.recorrer()

# d. Eliminar el personaje ubicado después de Jar Jar Binks
cola_personajes.eliminar_despues_de("Jar Jar Binks")

# Recorrer la cola después de la eliminación
print("\nCola después de eliminar el personaje después de Jar Jar Binks:")
cola_personajes.recorrer()
