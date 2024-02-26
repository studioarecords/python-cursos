nada = None
cadena = "Hola soy Victor Robles WEB"
cadena = "Desarrollador WEB"
entero = 99
flotante = 4.2
booleano = False
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("master", "en", "Python")
diccionario = {
    "nombre": "Victor",
    "apellido": "Robles",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"

# imprimir variable
print(nada)
print(cadena)

# mostrar tipo de dato Ej: <class 'NoneType'>
print(type(nada))
# mostrar tipo de dato Ej:  <class 'str'>
print(type(cadena))
print(dato_byte)

print(rango)

# ---------------------------------------------------------------------------------------#

# Convertir tipo de dato
texto = "Hola soy un texto"
numerito = str(776)
# 776
# "776"
print(texto + " " + numerito)
