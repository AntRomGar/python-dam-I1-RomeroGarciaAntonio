from datetime import datetime
from modulo_input import pedir_datos
from modulo_calculo import calcular_edad, clasificar_edad

# modulo_input.py
def pedir_datos():
    """
    Pide al usuario su nombre y año de nacimiento.
    Valida que el año sea un número entero.
    Devuelve una tupla (nombre, año_nacimiento).
    """
    nombre = input("Introduce tu nombre: ")
    while True:
        try:
            anio = int(input("Introduce tu año de nacimiento: "))
            return nombre, anio
        except ValueError:
            print("Por favor, introduce un año válido (número).")

# modulo_calculo.py

def calcular_edad(anio_nacimiento):
    """
    Calcula la edad actual a partir del año de nacimiento.
    """
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento

def clasificar_edad(edad):
    """
    Clasifica la edad en tramos:
    - Menor de 18
    - Entre 18 y 65
    - Mayor de 65
    """
    if edad < 18:
        return "Menor de edad (<18)"
    elif edad <= 65:
        return "Adulto (18-65)"
    else:
        return "Mayor de 65"

# prueba.py (archivo principal)

def main():
    # Pedimos los datos al usuario
    nombre, anio_nacimiento = pedir_datos()
    # Calculamos la edad
    edad = calcular_edad(anio_nacimiento)
    # Clasificamos la edad
    tramo = clasificar_edad(edad)
    # Mostramos el resultado
    print(f"\nHola {nombre}, tienes {edad} años. Clasificación: {tramo}")

if __name__ == "__main__":
    main()