buscar = 10
for numero in range(11):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
     print("no encontre el numero")       