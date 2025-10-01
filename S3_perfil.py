import datetime

# S3_perfil.py

# Definimos las variables que vamos a usar
nombre = ""
anio_nacimiento = 0
edad = 0
tramo = ""

# Pedir el nombre al usuario
nombre = input("Introduce tu nombre: ")

# Pedir el año de nacimiento y manejar errores
while True:
    try:
        anio_nacimiento = int(input("Introduce tu año de nacimiento (ejemplo: 2000): "))
        break
    except ValueError:
        print("Por favor, introduce un número válido para el año.")

# Calcular la edad
anio_actual = datetime.datetime.now().year
edad = anio_actual - anio_nacimiento

# Clasificar la edad en tramos
if edad < 18:
    tramo = "Menor de edad (<18)"
elif edad <= 65:
    tramo = "Adulto (18-65)"
else:
    tramo = "Adulto mayor (>65)"

# Mostrar el resultado
print(f"\nHola {nombre}, tienes {edad} años. Tu tramo de edad es: {tramo}")
