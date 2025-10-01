from datetime import datetime

# Programa para pedir el nombre y año de nacimiento, calcular la edad y clasificarla por tramos


def obtener_datos():
    nombre = input("Introduce tu nombre: ")
    while True:
        try:
            anio_nacimiento = int(input("Introduce tu año de nacimiento: "))
            break  # Sale del bucle si la conversión fue exitosa
        except ValueError:
            print("Por favor, introduce un número válido para el año.")
    return nombre, anio_nacimiento

def calcular_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento

def clasificar_edad(edad):
    if edad < 18:
        return "Menor de edad (<18)"
    elif 18 <= edad <= 65:
        return "Adulto (18-65)"
    else:
        return "Adulto mayor (>65)"

def main():
    nombre, anio_nacimiento = obtener_datos()
    edad = calcular_edad(anio_nacimiento)
    clasificacion = clasificar_edad(edad)
    print(f"\nHola {nombre}, tienes {edad} años. Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()