# Convierte una temperatura de Kelvin a Fahrenheit.
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Convierte una temperatura de Fahrenheit a Kelvin.
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

print("Conversor de temperaturas")
print("1. Kelvin a Fahrenheit")
print("2. Fahrenheit a Kelvin")
opcion = input("Selecciona una opción (1 o 2): ")

# Si el usuario selecciona la opción 1, 
# convierte de Kelvin a Fahrenheit.
if opcion == "1":
    kelvin = float(input("Introduce la temperatura en Kelvin: "))
    fahrenheit = kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin} K son {fahrenheit:.2f} °F")
# Si el usuario selecciona la opción 2, 
# convierte de Fahrenheit a Kelvin.
elif opcion == "2":
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    kelvin = fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit} °F son {kelvin:.2f} K") # Muestra el formato de las cadenas de numeros flotantes con 2 decimales
# Si la opción no es válida, muestra un mensaje de error.
else:
    print("Opción no válida.")