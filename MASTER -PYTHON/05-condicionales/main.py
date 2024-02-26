"""
# Operadores de comparacion 
== igual
!= diferente
< menor que 
> mayor que
<= menor o igual que 
>= mayor o igual que

# Operadores logicos
and Y
or  O
!   negacion
not NO

"""
""" # Ejemplo 1
print("###################### EJEMPLO 1######################")

# color = "verde"
color = input("Adivina cual e mi color favorito: ")
if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("Lo siento ")
    print("Color incorrecto")
"""
"""
# Ejemplo 2

print("######################### EJEMPLO 2 ######################### ")

# year = 2020
year = int(input("¿En que año estamos?: "))
if year >= 2021:
    print("Estamos en 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")
"""

"""
# Ejemplo 3

print("######################### EJEMPLO 3 ######################### ")
# If anidados me muestra el segundo if cuando la primera condicion se cumpla
nombre = "Alberto Lopardo"
ciudad = "Barcelona"
continente = "Europa"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!!")

    if continente != "Europa":
        print("El usuario no es europeo")
    else:
        print(f"Es europeo y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")
"""

# Ejemplo 4

print("\n######################### EJEMPLO 4 ######################### ")

# dia = int(input("introduce el dia de la semana: "))
dia = 2
"""
if dia == 1:
    print("lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("es miercoles")
        else:
            if dia == 4:
                print("es jueves")
            else:
                if dia == 5:
                    print("es viernes")
                else:
                    print("es fin de semana")
"""
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("es Fin de Semana")

# Ejemplo 5 and

print("\n######################### EJEMPLO 5 ######################### ")

edad_minima = 18
edad_maxima = 65
# edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No está en edad de trabajar")

# Ejemplo 6 or

print("\n######################### EJEMPLO 6 ######################### ")

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana :( ")

# Ejemplo 7 not

print("\n######################### EJEMPLO 7 ######################### ")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana :( ")

# Ejemplo 8 not

print("\n######################### EJEMPLO 8 ######################### ")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} No es un pais de habla hispana :(")
else:
    print(f"{pais} Si es un pais de habla hispana :) ")
