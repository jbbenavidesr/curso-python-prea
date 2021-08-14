# Scope
# LEGB: Local -> Enclosing -> Global -> Built In

x = 10
y = 2
z = 4

def funcion_externa():

    x = 5
    y = 3

    def funcion_interna():
        x = 7

        print(f"En funcion interna x = {x}, y = {y} y z = {z}")

    print(f"En funcion externa x = {x}, y = {y} y z = {z}")

    return funcion_interna()

print(f"En el main x = {x}, y = {y} y z = {z}")


funcion_externa()

# funcion_interna() No esta definido

weight = 10

def add_weight(n):
    """Increase the weight  by n units"""
    global weight # Sin esto hay error, pero no es una buena práctica.
    weight = weight + n

add_weight(10)

print(weight)
