# Solicita al usuario un número entero.
num = int(input("Introduce un número: "))
if num < 2:                                 # Verifica si el número es menor que 2, ya que los números menores que 2 no son primos.      
    print("No es primo")
else:
    es_primo = True                         # Inicializa una variable para determinar si el número es primo.
    for i in range(2, int(num ** 0.5) + 1): # Itera desde 2 hasta la raíz cuadrada del número (incluyendo el entero más cercano).
        if num % i == 0:                    # Si el número es divisible por algún número en este rango, no es primo.
            es_primo = False
            break
    if es_primo:                            # Si no se encontró ningún divisor, el número es primo.
        print("Es primo")
    else:
        print("No es primo")