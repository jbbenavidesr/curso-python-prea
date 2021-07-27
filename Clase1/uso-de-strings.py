# Almaceno la informacion que le voy a mostrar al usuario
mensaje = "Bienvenido!\nEste es un saludo."

print(mensaje)

# Yo puedo pedirle a Python la longitud de un string
longitud_de_mensaje = len(mensaje)

print("El mensaje tiene", longitud_de_mensaje, "caracteres.")

# Puedo acceder a caracteres especificos
print(mensaje[0])  # Empieza a contar en 0, este es el primer caracter
print(mensaje[4])  # El caracter en la posición 5

# print(mensaje[30])  # Esto me va a dar un error

print(mensaje[-1])  # Muestra el último caracter
print(mensaje[-4])  # Muestra el cuarto caracter de atras pa adelante

# mensaje[3] = "h"  # No puedo asignar una letra nueva.
