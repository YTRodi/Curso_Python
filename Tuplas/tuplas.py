# --------------------------------------------------- TUPLAS
# Son inmutables, como los strings.
mi_tupla = (1,2,3)
print(type(mi_tupla))
print(mi_tupla)


mi_lista = [1,2,3]
print(type(mi_lista))
print(mi_lista)

mi_tupla[0] = 1000 # ERROR, dado que son inmutables
mi_lista[0] = 9999