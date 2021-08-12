# Loops

# While loop
# Se repite mientras que una condicion permanezca siendo verdadera
n = 0

#while condicion:
while n < 5:
    # Cuerpo: codigo que se repite mientras condicion sea verdad
    print(n)

    n = n + 1  # Si no pongo esto, n siempre es 0 y la condición es siempre verdad.
    # Eso sería un loop infinito.

# Ejemplo de uso en validation.py

# For loop
# Se repite para cada elemento de una coleccion
# Por ejemplo, cada caracter de un string
word = "Python"

for letter in word:
    print(letter)


# El for sirve para repetir algo un determinado numero de veces
# for i in range(n) repite el loop n veces con i pasando de 0 a n
for i in range(5): # Va de 0 a 4, el 5 no se cuenta.
    print(i)


# También se puede especificar el rango que se va a usar
for i in range(3, 6): # Este se repite 3 veces para valores de 3 al 5.
    print(i)



# Nested loops
# Se puede poner loops dentro de loops
for i in range(5):
    for j in range(3):
	print(f"i es {i} y j es {j}")

# mas profundo
for i in range(5):
    for j in range(3):
	for k in range(2):
	    print(f"i = {i}, j = {j} y k = {k}")


# o con while
for i in range(5):
    j = i
    while j < 5:
	print(f"i es {i} y j es {j}")
	j += 1

# Para entender mejor como corre el nested loop
for i in range(5):
    print(f"Esta empezando la iteracion {i} del loop de afuera")
    
    for j in range(4):
	print(f"Loop interno: j  es {j}, i es {i}")
		
    print("termina loop interno")



