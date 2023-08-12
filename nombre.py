# Nombres de variables
# Una variable puede tener un nombre corto ( como x e y ) o un nombre más descriptivo ( edad, nombre del coche, volumen_total ). Reglas para las variables de Python:
# Un nombre de variable debe comenzar con una letra o el carácter de subrayado
# Un nombre de variable no puede comenzar con un número
# Un nombre de variable solo puede contener caracteres alfanuméricos y guías bajos ( Az, 0-9 y _ )
# Los nombres de las variables distinguen entre mayúsculas y minúsculas ( edad, Edad y EDAD son tres variables diferentes )
# Un nombre de variable no puede ser ninguna de las palabras clave de Python .

# Nombres de variables legales:

myvar = "John"
my_var = "John"
_my_var = "John"

myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)

print(myVar)
print(MYVAR)
print(myvar2)


# Nombre de variables ilegales

# 2myvar = "John"
# my-var = "John"
# my var = "John"


# NOMBRE DE VARIABLES DE VARIAS PALABRAS

# Camel Case:
# Cada palabra, excepto la primera, comienza con una letra mayúscula:

myVariableName = "John"

# Pascal Case:
# Cada palabra comienza con una letra mayúscula:

MyVariableName = "John"

# Snake Case:
# Cada palabra está separada por un carácter de subrayado:

my_variable_name = "John"

print("\n")
# Muchos valores para múltiples variables
# Python le permite asignar valores a múltiples variables en una línea:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("\n")
# Un valor para múltiples variables
# Se puede asignar el mismo valor a múltiples variables en una línea:


a = b = c = "Orange"
print(a)
print(b)
print(c)

print("\n")
# Desempaquetar una colección
# Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en variables. Esto se llama desempacar.

fruits = ["apple", "banana", "cherry"]
d, e, f = fruits
print(d)
print(e)
print(f)
