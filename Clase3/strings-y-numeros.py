# Strings y numeros

# Un String que tiene un numero, se puede transformar a un numero
# int() para enteros o float() para decimales
numero = int("20")
decimal = float("3.1415")

#pasar de un numero a un string
string = str(10)

print(numero, decimal)

# Los operadores cambian si es string o numero
# + suma o concatena
# * entre 2 numeros multiplica y
# entre un string y un entero, concatena muchas veces

print(2 + 2)
print("hola" + " mundo")
print(3 * 4)
print("Hola" * 3)

# f-strings
edad = 10
nombre = "Juan"

print("Tengo " + str(edad) + " años")

print(f"Hola, soy {nombre} y tengo {edad} años.")
