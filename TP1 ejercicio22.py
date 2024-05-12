
def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    if indice >= len(mochila):
        return -1, objetos_sacados  
    elif mochila[indice] == "sable de luz":
        return indice, objetos_sacados + 1  
    else:
        return usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)

mochila = ["comida", "mapa", "sable de luz", "botiquín"]
indice_sable, objetos_sacados = usar_la_fuerza(mochila)
if indice_sable != -1:
    print("Se encontró un sable de luz en la posición", indice_sable, "y se sacaron", objetos_sacados, "objetos.")
else:
    print("No se encontró un sable de luz en la mochila.")
