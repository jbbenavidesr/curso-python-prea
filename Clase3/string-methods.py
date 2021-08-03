# Metodos de Strings

# Un método es una función que hace parte de un objeto.
# Ejemplo

#Mi objeto: Un string
objeto = "Hola mundo"

# Una función es independiente y le paso mi objeto
len(objeto)

# Un método hace parte de mi objeto
objeto.upper() # Lo vuelve todo mayuscula
objeto.lower() # Lo vuelve todo minuscula
objeto.title() # La primera letra de cada palabra en mayuscula


# Puedo encadenarlos: Si el resultado del metodo es otro string
# se puede volver a aplicar otro método
print(objeto.lower().replace("h", "H"))

# Metodos para eliminar espacios vacios al comienzo y al final
nombre= "       Juan Bernardo             "

# Elimina espacio vacio al comienzo
print(nombre.lstrip())
# Elimina espacio vacio al final
print(nombre.rstrip())
# Elimina espacio vacio al comienzo y al final
print(nombre.strip())

# Cambiar caracteres
print(nombre.strip().replace(" ", "_"))


# Identificar si comienza o termina con algo
print(objeto.startswith("H"))
print(objeto.endswith("ndo"))

# Si no es asi
print(objeto.startswith("h"))
print(objeto.endswith("u"))
