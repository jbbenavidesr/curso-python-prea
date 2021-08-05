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

# find
# Encuentra un substring en otro y devuelve el indice donde comienza
objeto.find("mun") # Devuelve el numero 5 que es donce comienza "mun"

objeto.find("juan") # Devuelve -1 porque no existe

# Solo encuentra la primera vez
mensaje = "quiero muchas papas, porque me gustan las papas"
mensaje.find("papas") # solo devuelve el indice de la primera vez que dice papas

# Replace 
# Este metodo lo que hace es reemplaar una parte por otro string
# Este si reemplaza todas las ocurrencias
mensaje.replace("papas", "tomates") # Devuelve: "quiero muchas tomates, porque me gustan las tomates"
