# comillas simples dentro de comillas doble funciona como string
mi_texto = ' "Master" '

# \ barra deshabilita la funcion de comillas a string
mi_texto2 = "en \"Python\" "

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

# salto de linea \n
texto_unido = mi_texto + " \n " + mi_texto2
print(texto_unido)

# tabulacion o espacio  \t
texto_unido = mi_texto + " \t " + mi_texto2
print(texto_unido)

# borra \r lo anterior
texto_unido = mi_texto + " \r " + mi_texto2
print(texto_unido)
