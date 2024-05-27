class PilaMCU:
    def __init__(self):
        self.pila = []

    def apilar(self, personaje):
        self.pila.append(personaje)

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        return None

    def esta_vacia(self):
        return len(self.pila) == 0

    def cima(self):
        if not self.esta_vacia():
            return self.pila[-1]
        return None

    def tamanio(self):
        return len(self.pila)
    
    #determinar la posición de Rocket Raccoon y Groot

def posicion_personaje(pila, nombre):
    pila_aux = PilaMCU()
    posicion = 1

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['nombre'] == nombre:
            break
        posicion += 1

        #apilar los elementos en la pila original

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    if posicion > pila.tamanio():
        return -1
    return posicion

#determinar los personajes que participaron en más de 5 películas

def personajes_mas_de_5_peliculas(pila):
    personajes = []
    pila_aux = PilaMCU()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['peliculas'] > 5:
            personajes.append((personaje['nombre'], personaje['peliculas']))

            #apilar los elementos en la pila original

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return personajes

#determinar cuántas películas participó Black Widow

def peliculas_viuda_negra(pila):
    pila_aux = PilaMCU()
    peliculas = 0

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['nombre'] == 'Black Widow':
            peliculas = personaje['peliculas']

       #apilar los elementos en la pila original     

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return peliculas

#función para mostrar personajes cuyos nombres empiezan con C, D y G

def personajes_con_letras(pila):
    personajes = []
    pila_aux = PilaMCU()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['nombre'][0] in 'CDG':
            personajes.append(personaje['nombre'])

    #apilar los elementos en la pila original

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return personajes

if __name__ == "__main__":
    pila_mcu = PilaMCU()
    pila_mcu.apilar({'nombre': 'Iron Man', 'peliculas': 10})
    pila_mcu.apilar({'nombre': 'Captain America', 'peliculas': 9})
    pila_mcu.apilar({'nombre': 'Thor', 'peliculas': 8})
    pila_mcu.apilar({'nombre': 'Black Widow', 'peliculas': 7})
    pila_mcu.apilar({'nombre': 'Hulk', 'peliculas': 5})
    pila_mcu.apilar({'nombre': 'Hawkeye', 'peliculas': 4})
    pila_mcu.apilar({'nombre': 'Rocket Raccoon', 'peliculas': 6})
    pila_mcu.apilar({'nombre': 'Groot', 'peliculas': 5})

    print("Posición de Rocket Raccoon:", posicion_personaje(pila_mcu, 'Rocket Raccoon'))
    print("Posición de Groot:", posicion_personaje(pila_mcu, 'Groot'))
    print("Personajes en más de 5 películas:", personajes_mas_de_5_peliculas(pila_mcu))
    print("Películas en las que participó Black Widow:", peliculas_viuda_negra(pila_mcu))
    print("Personajes cuyos nombres empiezan con C, D y G:", personajes_con_letras(pila_mcu))

    
        