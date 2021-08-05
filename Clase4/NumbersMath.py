# Numeros y matemáticas

# Enteros: tipo int
print(type(4))

# Para poner numeros grandes se puede usar raya al piso
millon = 1_000_000

print(type(millon))

# float
print(type(4.0))
millon = 1_000_000.0

print(type(millon))

# Puedo usar notacion cientifica
millon = 1e6
milesima = 1e-3

print(millon, milesima)

# Tienen un limite y luego le pone el nombre inf
print(1e400)


# Aritmetica

# Sumas
a = 10 + 5
b = 10 + 5.8

# Restas
c = 50 - 3
d = 2.4 - 4.3

# Multiplicacion
e = 3 * 5
f = 3.8 * 9

# Division (siempre float)
g = 4 / 2
h = 4.8 / 3.5

# Division Entera
i = 4 // 2
j = 7.3 // 2.3

# exponentes
k = 2 ** 3
l = 3 ** 0.5

# modulo (Solo con enteros)
m = 5 % 2 
n = 29 % 4

# Orden de operaciones funciona normal
o = 2 * 4 - 5 # 3
p = 2 * (4 - 5) # -2

# Funciones para numeros

# round: entero mas cercano
print(round(7.3))

pi_entero = round(3.1415926)
pi_4decimales = round(3.1415926, 4)

print(pi_entero)
print(pi_4decimales)

# abs: valor absoluto
print(abs(-10))

# pow: power
print(pow(2, 3))
print(pow(2, 3, 3))


