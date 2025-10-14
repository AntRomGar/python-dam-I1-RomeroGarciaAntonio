# Solicita al usuario una lista de números separados por comas,
# los procesa y devuelve una lista de números flotantes.
def pedir_lista_numeros():
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = []
    for valor in entrada.split(","):
        try:
            num = float(valor.strip())
            numeros.append(num)
        except ValueError:
            print(f"Valor inválido ignorado: '{valor.strip()}'")
    return numeros

# Recibe una lista de números y calcula estadísticas 
# básicas como suma, media, máximo y duplicados.
def mostrar_estadisticas(numeros):
    if not numeros:
        print("No se ingresaron números válidos.")
        return
    suma = sum(numeros)
    media = suma / len(numeros)
    maximo = max(numeros)
    duplicados = set([x for x in numeros if numeros.count(x) > 1])
    print(f"Suma: {suma}")
    print(f"Media: {media}")
    print(f"Máximo: {maximo}")
    print(f"Duplicados: {', '.join(map(str, duplicados)) if duplicados else 'Ninguno'}")
    # Muestra los números duplicados en la lista, separados por comas. Si no hay duplicados, muestra 'Ninguno'.
    # 1. map(str, duplicados): Convierte cada número duplicado en una cadena.
    # 2. ', '.join(...): Une las cadenas resultantes con comas y espacios.
    # 3. if duplicados else 'Ninguno': Si el conjunto duplicados está vacío, muestra 'Ninguno'.


# Punto de entrada principal del programa. Ejecuta las funciones 
# para pedir números y mostrar estadísticas si el archivo se ejecuta directamente.
if __name__ == "__main__":
    numeros = pedir_lista_numeros()
    mostrar_estadisticas(numeros)