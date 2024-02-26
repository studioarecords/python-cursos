""""
Una variable es un contenedor de informacion 
que dentro guardará un dato, se pueden crear muchas variables y que cada una tenga un dato distiinto
"""

# variables y asignarles un valor
texto = "Master en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

# Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------------")

# Sustituir el valor de algunas variables / reasignando valores
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("------------------------------------")


# Concatenación

nombre = "Victor"
apellidos = "Robles"
web = "victorrobles.es"


print(nombre+" "+apellidos+" - "+web)
# Otra manera de dar formato a strings con f y llaves
print(f"{nombre} {apellidos} - {web}")
# Metodo .format
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web)
