# Diferencias entre un array y una lista:
#  -La lista puede almacenar otras cosas además de carácteres (Palabras, decimales, tipos completos)
friends = [] #Array
friends2 = list() # Retorna una lista vacia

friends.append('Pepe')
friends.append('Juan')
friends.append('Agustin')
friends.append(100)
print(friends)


grupo = list()

grupo.append("GRUPO A")
grupo.append(2)
grupo.append("GRUPO B")
grupo.append(50)

print(grupo)