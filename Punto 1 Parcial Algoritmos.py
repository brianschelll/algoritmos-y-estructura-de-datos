def imprimir_inverso(lista):
    
    if not lista:
        return
    
    print(lista[-1])
    
    imprimir_inverso(lista[:-1])

mi_lista = [1, 2, 3, 4, 5]
imprimir_inverso(mi_lista)
