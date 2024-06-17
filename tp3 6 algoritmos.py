super_heroes = [
  {
      "nombre": "Linterna Verde",
      "año_aparicion": 1940,
      "casa_comic": "DC Comics",
      "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
      "nombre": "Wolverine",
      "año_aparicion": 1974,
      "casa_comic": "Marvel Comics",
      "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
      "nombre": "Doctor Strange",
      "año_aparicion": 1963,
      "casa_comic": "Marvel Comics",
      "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
      "nombre": "Capitana Marvel",
      "año_aparicion": 1968,
      "casa_comic": "Marvel Comics",
      "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
      "nombre": "Mujer Maravilla",
      "año_aparicion": 1941,
      "casa_comic": "DC Comics",
      "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
      "nombre": "Flash",
      "año_aparicion": 1940,
      "casa_comic": "DC Comics",
      "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
      "nombre": "Star-Lord",
      "año_aparicion": 1976,
      "casa_comic": "Marvel Comics",
      "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
      "nombre": "Superman",
      "año_aparicion": 1938,
      "casa_comic": "DC Comics",
      "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
      "nombre": "Batman",
      "año_aparicion": 1939,
      "casa_comic": "DC Comics",
      "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
      "nombre": "Iron Man",
      "año_aparicion": 1963,
      "casa_comic": "Marvel Comics",
      "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
      "nombre": "Wonder Woman",
      "año_aparicion": 1941,
      "casa_comic": "DC Comics",
      "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
      "nombre": "Spider-Man",
      "año_aparicion": 1962,
      "casa_comic": "Marvel Comics",
      "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
      "nombre": "Thor",
      "año_aparicion": 1962,
      "casa_comic": "Marvel Comics",
      "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
      "nombre": "Aquaman",
      "año_aparicion": 1941,
      "casa_comic": "DC Comics",
      "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
      "nombre": "Green Arrow",
      "año_aparicion": 1941,
      "casa_comic": "DC Comics",
      "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
      "nombre": "Hulk",
      "año_aparicion": 1962,
      "casa_comic": "Marvel Comics",
      "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
      "nombre": "Black Widow",
      "año_aparicion": 1964,
      "casa_comic": "Marvel Comics",
      "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
      "nombre": "Mr. Fantástico",
      "año_aparicion": 1961,
      "casa_comic": "Marvel Comics",
      "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
      "nombre": "La Mujer Invisible",
      "año_aparicion": 1961,
      "casa_comic": "Marvel Comics",
      "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
      "nombre": "La Antorcha Humana",
      "año_aparicion": 1961,
      "casa_comic": "Marvel Comics",
      "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
      "nombre": "La Cosa",
      "año_aparicion": 1961,
      "casa_comic": "Marvel Comics",
      "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
      "nombre": "Capitán América",
      "año_aparicion": 1941,
      "casa_comic": "Marvel Comics",
      "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
      "nombre": "Ant-Man",
      "año_aparicion": 1962,
      "casa_comic": "Marvel Comics",
      "biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }
]

# Función para eliminar el nodo que contiene la información de Linterna Verde
def eliminar_linterna_verde(superheroes):
  for idx, heroe in enumerate(superheroes):
      if heroe["nombre"] == "Linterna Verde":
          del superheroes[idx]
          break

# Función para mostrar el año de aparición de Wolverine
def aparicion_wolverine(superheroes):
  for heroe in superheroes:
      if heroe["nombre"] == "Wolverine":
          return heroe["año_aparicion"]

# Función para cambiar la casa de Dr. Strange a Marvel
def cambiar_casa_dr_strange(superheroes):
  for heroe in superheroes:
      if heroe["nombre"] == "Doctor Strange":
          heroe["casa_comic"] = "Marvel Comics"
          break

# Función para mostrar el nombre de superhéroes que mencionan "traje" o "armadura" en su biografía
def buscar_biografia(superheroes, palabra_clave):
  nombres = []
  for heroe in superheroes:
      if palabra_clave in heroe["biografia"].lower():
          nombres.append(heroe["nombre"])
  return nombres

# Función para mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def aparicion_anterior_1963(superheroes):
  resultados = []
  for heroe in superheroes:
      if heroe["año_aparicion"] < 1963:
          resultados.append((heroe["nombre"], heroe["casa_comic"]))
  return resultados

# Función para mostrar la casa de Capitana Marvel y Mujer Maravilla
def casa_capitana_marvel_y_mujer_maravilla(superheroes):
  casa_capitana_marvel = ""
  casa_mujer_maravilla = ""
  for heroe in superheroes:
      if heroe["nombre"] == "Capitana Marvel":
          casa_capitana_marvel = heroe["casa_comic"]
      elif heroe["nombre"] == "Mujer Maravilla":
            casa_mujer_maravilla = heroe["casa_comic"]
  return casa_capitana_marvel, casa_mujer_maravilla

# Función para mostrar toda la información de Flash y Star-Lord
def informacion_flash_y_star_lord(superheroes):
    flash_info = {}
    star_lord_info = {}
    for heroe in superheroes:
        if heroe["nombre"] == "Flash":
            flash_info = heroe.copy()
        elif heroe["nombre"] == "Star-Lord":
            star_lord_info = heroe.copy()
    return flash_info, star_lord_info

# Función para listar los superhéroes que comienzan con la letra B, M y S
def superheroes_por_letra(superheroes, letras):
    nombres = []
    for heroe in superheroes:
        if heroe["nombre"][0].upper() in letras:
            nombres.append(heroe["nombre"])
    return nombres

# Función para determinar cuántos superhéroes hay de cada casa de comic
def contar_superheroes_por_casa(superheroes):
    conteo = {"Marvel Comics": 0, "DC Comics": 0}
    for heroe in superheroes:
        if heroe["casa_comic"] == "Marvel Comics":
            conteo["Marvel Comics"] += 1
        elif heroe["casa_comic"] == "DC Comics":
            conteo["DC Comics"] += 1
    return conteo

# Ejemplos de uso de las funciones:

# a. Eliminar el nodo que contiene la información de Linterna Verde
eliminar_linterna_verde(super_heroes)
print("Lista de superhéroes después de eliminar a Linterna Verde:")
for heroe in super_heroes:
    print(heroe["nombre"])

# b. Mostrar el año de aparición de Wolverine
print("\nAño de aparición de Wolverine:", aparicion_wolverine(super_heroes))

# c. Cambiar la casa de Dr. Strange a Marvel
cambiar_casa_dr_strange(super_heroes)
print("\nCasa de Dr. Strange después del cambio:", [heroe["casa_comic"] for heroe in super_heroes if heroe["nombre"] == "Doctor Strange"][0])

# d. Mostrar el nombre de superhéroes que mencionan "traje" o "armadura" en su biografía
print("\nSuperhéroes que mencionan 'traje' o 'armadura':", buscar_biografia(super_heroes, "traje") + buscar_biografia(super_heroes, "armadura"))

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
print("\nSuperhéroes con aparición anterior a 1963:")
for nombre, casa in aparicion_anterior_1963(super_heroes):
    print(f"{nombre} - {casa}")

# f. Mostrar la casa de Capitana Marvel y Mujer Maravilla
casa_capitana_marvel, casa_mujer_maravilla = casa_capitana_marvel_y_mujer_maravilla(super_heroes)
print("\nCasa de Capitana Marvel:", casa_capitana_marvel)
print("Casa de Mujer Maravilla:", casa_mujer_maravilla)

# g. Mostrar toda la información de Flash y Star-Lord
flash_info, star_lord_info = informacion_flash_y_star_lord(super_heroes)
print("\nInformación de Flash:")
print(flash_info)
print("\nInformación de Star-Lord:")
print(star_lord_info)

# h. Listar los superhéroes que comienzan con la letra B, M y S
letras = ['B', 'M', 'S']
for letra in letras:
    print(f"\nSuperhéroes que empiezan con la letra '{letra}':")
    print(superheroes_por_letra(super_heroes, letra))

# i. Determinar cuántos superhéroes hay de cada casa de comic
conteo_casas = contar_superheroes_por_casa(super_heroes)
print("\nCantidad de superhéroes por casa de cómic:")
print("Marvel Comics:", conteo_casas["Marvel Comics"])
print("DC Comics:", conteo_casas["DC Comics"])

