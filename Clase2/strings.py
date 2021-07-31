## Strings

mensaje = "Este es el string de prueba para entendernos"

# Encontrar el largo de un string
longitud = len(mensaje)
print(longitud)


# Escape
#String con caracteres especiales
"Juan le dijo que \"si pretendo llegar a tiempo,\
debo salir ya\" "


# Concatenar
nombre = "Hans"
apellido = "Morales"
nombre_completo = nombre + " " + apellido

print(nombre_completo)

# Index
# h | o | l | a
# 0   1   2   3
#-4  -3  -2  -1
primera_letra = mensaje[0]
ultima_letra = mensaje[-1]
caracter_en_posicion_14 = mensaje[13] # arranca en 0

# Slicing
# | h | o | l | a |
# 0   1   2   3   4
#-4  -3  -2  -1

prueba = "hola"
comienzo = prueba[0:2]
fin = prueba[2:4]
no_existe = prueba[15:20]

para_atras = prueba[-2:-4]

desde_el_comienzo = prueba[:2]
hasta_el_final = prueba[1:]

# Challenge!
mensaje = "Este no esta bien"

# El reto es que se imprima "Esto no esta bien"
print(mensaje)



