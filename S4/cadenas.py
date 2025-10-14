cadena = input("Introduce una cadena: ")

vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

num_vocales = sum(1 for c in cadena if c in vocales)         # Cuenta las letras vocales
num_consonantes = sum(1 for c in cadena if c in consonantes) # Cuenta las letras consonantes
num_mayusculas = sum(1 for c in cadena if c.isupper())       # Cuenta las letras mayúsculas y devuelve el total de mayúsculas
num_caracteres = len(cadena)                                 # Cuenta todos los caracteres en la cadena

print(f"Número de vocales: {num_vocales}")
print(f"Número de consonantes: {num_consonantes}")
print(f"Número de mayúsculas: {num_mayusculas}")
print(f"Número de caracteres: {num_caracteres}")