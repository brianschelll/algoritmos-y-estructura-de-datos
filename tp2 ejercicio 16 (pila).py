def interseccion_de_personajes(personajes1, personajes2):
    list1 = []
    list2 = []

    # Desapilar personajes episodio V
    while personajes1:
        list1.append(personajes1.pop())

    # Desapilar personajes episodio VII
    while personajes2:
        list2.append(personajes2.pop())

    # Intersección de personajes entre ambas películas
    interseccion = list(set(list1) & set(list2))
    
    return interseccion

personajes_episodioV = ["luke", "han", "leia", "yoda", "boba fett"]
personajes_episodioVII = ["rey", "finn", "han", "leia", "kylo ren"]

personajes_de_ambas_peliculas = interseccion_de_personajes(personajes_episodioV.copy(), personajes_episodioVII.copy())

print('Los personajes que aparecen en ambas películas son:', personajes_de_ambas_peliculas)



