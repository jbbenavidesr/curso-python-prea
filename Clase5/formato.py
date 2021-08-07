# Format

# Se puede dar formato a la forma en que se imprimen los numeros

# Un numero especifico de decimales redondeando
pi = 3.1415926

print(f"El valor de pi a 3 decimales es {pi:.2f}")

# Numeros grandes usando comas
mucho = 123456789

print(f"El número {mucho:,} es muy grande")

# Se pueden juntar
deudas = 1367298.826537

print(f"Le debo ${deudas:,.2f}")

# Se pueden mostrar como porcentajes con un dado numero de decimales

mitad = 0.5

print(f"Los estudios muestran que el {mitad:.1%} de las personas son la mitad del grupo.")
