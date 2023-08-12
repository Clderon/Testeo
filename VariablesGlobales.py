# Variables globales
# Las variables que se crean fuera de una función (como en todos los ejemplos anteriores)
# se conocen como variables globales. Las variables globales pueden ser utilizadas por todos,
# tanto dentro como fuera de las funciones.


# Crear una variable fuera de una función y usarla dentro de la función

x = "increible"


def myfunc():
    print("Python es " + x)


myfunc()


print("\n")
# Si se crea una variable con el mismo nombre dentro de una función, esta variable será local y
# solo se puede usar dentro de la función. La variable global con el mismo nombre quedará como estaba,
# global y con el valor original.

# Crear una variable dentro de una función, con el mismo nombre que la variable global

x = "increible"


def myfunc():
    x = "fantastico"
    print("Python es " + x)


myfunc()
print("Python es " + x)


print("\n")
# global Keyword
# Normalmente, cuando crea una variable dentro de una función, 
# esa variable es local y solo se puede usar dentro de esa función.
# Para crear una variable global dentro de una función, puede usar la palabra clave global.

def myfunc():
  global x
  x = "fantastico"

myfunc()

print("Python es " + x)


print("\n")
# Para cambiar el valor de una variable global dentro de una función, consulte la variable utilizando la palabra clave global:

x = "increible"

def myfunc():
  global x
  x = "fantastico"

myfunc()

print("Python es " + x)
