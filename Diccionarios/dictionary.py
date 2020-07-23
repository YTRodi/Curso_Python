# --------------------------------------------------- DICIONARIOS (Clave, valor)
my_dictionary = dict() # 1 de declarar un diccionario
my_dictionary = {} # 2 de declarar un diccionario
my_dictionary['primer_elemento'] = 'Hello'
my_dictionary['segundo_elemento'] = 'Bye'
my_dictionary[2] = 21

print(my_dictionary['primer_elemento'])
print(my_dictionary[2])

calificaciones = {}
calificaciones['Matemáticas'] = 7
calificaciones['Programación'] = 9
calificaciones['Laboratorio'] = 10
calificaciones['Pasteleria'] = 4

# IMPRIMO SOLO LAS CLAVES
for key in calificaciones:
    print(key)

# IMPRIMO SOLO LOS VALORES
for value in calificaciones.values():
    print(value)

# IMPRIMO LAS CLAVES Y LOS VALORES
for key,value in calificaciones.items():
    print('llave:{} - valor:{}'.format(key,value))


suma_calificaciones = 0
for calificacion in calificaciones.values():
    suma_calificaciones += calificacion

promedio = suma_calificaciones / len(calificaciones.values())

print("Suma de las calificaciones: {}".format(suma_calificaciones))
print('Promedio de calificaciones: {}'.format(promedio))