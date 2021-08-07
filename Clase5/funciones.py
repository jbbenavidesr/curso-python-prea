# Funciones

# Son valores y se pueden asignar a variables.

print(type(len)) # Built in function

# El nombre len es solo una variable y se puede reasignar

len = "ahora soy string"
print(type(len)) # string


# No es recomendado hacer esto nunca para funciones built in

del len
print(type(len)) # Built in function otra vez

# La funcion como tal es como una maquina que existe.
# Para usarla hay que llamarla con los parentesis
# Y entregarle los valores que necesita para trbajar (los parametros)

four = len("four") #Esta recibe un parametro y devuelve un numero
# Python asigna ese numero del resultado, no la funcion
four = 4 # Despues de correr es como si reemplazara la funcion por el resultado.


# Algunas funciones tienen efectos secundarios
lo_impreso = print("Qué devuelvo?") # Esta funcion pone el valor en la consola

# Pero no devuelve nada...
# En python una función siempre devuelve algo, 
# si no es nada es este objeto de tipo NoneType
print(lo_impreso)
print(type(lo_impreso)) 


# Puedo asignar una función a otra variable
imprimir = print

imprimir("Ahora este nombre apunta a la misma función")
print("Pero este también, eso no se cambia")

DRY = "Don't Repeat Yourself"

# Puedo crear mis funciones para no repetir codigo

# Para eso las defino en una firma
def sumar(a, b): # Esta es la firma con def nombre (parametros):
    # El cuerpo va indentado y tiene
    # Docstring que describe que hace la función
    """Suma los valores a y b"""
    # El codigo, es una plantilla que se corre al llamar la función
    result = a + b

    # Lo que devuelve la función, si no se pone devuelve None
    return result

    # Lo que pase después del return ya no importa, python para ahí

# La función se acaba cuando hay codigo que ya no esta indentado.


# Se llama la función con el nombre y los parametros. 
suma = sumar(4, 2)


print(suma)

 
