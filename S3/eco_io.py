try:
    # Pide al usuario que ingrese tres notas entre 0 y 100
    nota1 = float(input("Introduce la primera nota (0-100): "))
    nota2 = float(input("Introduce la segunda nota (0-100): "))
    nota3 = float(input("Introduce la tercera nota (0-100): "))

    # Comprueba que las notas estén en el rango correcto
    if not (0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100):
        print("Error: Todas las notas deben estar entre 0 y 100.")
    else:
        # Calcula la suma de las notas
        suma = nota1 + nota2 + nota3

        # Calcula la media de las notas
        media = suma / 3

        # Encuentra la nota mayor
        mayor = max(nota1, nota2, nota3)

        # Muestra los resultados
        print("Suma de las notas:", suma)
        print("Media de las notas:", media)
        print("La nota mayor es:", mayor)

        # Comprueba si la media es suficiente para aprobar
        if media >= 50:
            print("¡Aprobado!")
        else:
            print("Suspenso.")
except ValueError:
    print("Error: Debes introducir un número válido para las notas.")