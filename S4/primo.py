# Solicita al usuario un número entero.
num = int(input("Introduce un número: "))

# Verifica si el número es menor que 2, ya que los números menores que 2 no son primos.
if num < 2:
    print("No es primo")
else:
    # Inicializa una variable para determinar si el número es primo.
    es_primo = True
    # Itera desde 2 hasta la raíz cuadrada del número (incluyendo el entero más cercano).
    for i in range(2, int(num ** 0.5) + 1):
        # Si el número es divisible por algún número en este rango, no es primo.
        if num % i == 0:
            es_primo = False
            break
    # Si no se encontró ningún divisor, el número es primo.
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")