# La función Python print() se usa a menudo para generar variables.

x = "Luis miguel calderon carlos"
print(x)

print("\n")
# En la función print(), genera múltiples variables, separadas por una coma:

x = "Python"
y = "es"
z = "increible"

# La mejor manera de generar múltiples variables en la función print() es separarlas con comas, que incluso admiten diferentes tipos de datos:
print(x, y, z)

# También puede usar el operador + para generar múltiples variables (esta opcion no genera espaciado):
print(x + y + z)

# Para números, el carácter + funciona como un operador matemático.
x = 5
y = 10
print(x + y)

# En la función print(), cuando intenta combinar una cadena y un número con el operador +, Python dará un error:
