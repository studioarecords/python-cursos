edad = int(input("Ingrese su edad: "))

# las evaluaciones se hacen de arriba hacia abajo
if edad >= 54:
    print("tienes un descuento")
elif edad > 17:
    print("puedes ver la pelicula")
else:
    print("no puedes ver la pelicula")
    print("ve a otro lado")
    
print("Listo")