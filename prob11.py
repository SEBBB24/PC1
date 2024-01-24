#Usando diccionarios, aunque el orden de la lista no necesariamente es el mismo que el original, coincide con lo solicitado

mi_lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(dict.fromkeys(mi_lista))

lista_sin_duplicados