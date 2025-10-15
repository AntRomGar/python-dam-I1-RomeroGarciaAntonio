from collections import Counter  # Importa Counter para contar frecuencia de calificaciones.

def pedir_notas():
    
    #Solicita al usuario una lista de calificaciones separadas por comas.
    #Valida cada entrada y solo acepta valores numéricos válidos entre 0 y 10.
    
    notas = []                                                                         # Lista vacía donde se guardarán las calificaciones válidas.

    notas_str = input("Introduce las calificaciones separadas por comas: ") # Solicita al usuario una cadena con notas separadas por comas.
    partes = notas_str.split(",")  # Divide la cadena en partes individuales usando la coma como separador.

    for parte in partes:  # Recorre cada parte de la lista para procesar cada calificación.
        nota_limpia = parte.strip()   # Elimina espacios en blanco alrededor de la calificación.

        if nota_limpia:     # Verifica que la entrada no esté vacía (por si hay comas seguidas).
            try:
                nota = float(nota_limpia)  # Intenta convertir la entrada a número decimal.

                if 0 <= nota <= 10: # Verifica que la nota esté en el rango válido (0 a 10).
                    notas.append(nota)  # Si es válida, la agrega a la lista de notas.
                else:
                    print(f"Nota fuera de rango (0-10): '{nota_limpia}' → Ignorada.")  # Si está fuera de rango, muestra advertencia.
            except ValueError:
                print(f"Entrada inválida: '{nota_limpia}' no es un número → Ignorada.")  # Si no se puede convertir a número, muestra error.

    return notas   # Devuelve la lista final con solo las calificaciones válidas.


def resumen_estadistico(notas):
    # Calcula un resumen estadístico de las calificaciones: total, media, mínima y máxima.

    total = len(notas)  # len() devuelve la cantidad de elementos en la lista 'notas'.

    media = round(sum(notas) / total, 2) if total > 0 else 0  
    # Calcula la media (promedio) solo si hay al menos una nota.
    # sum(notas) suma todos los valores.
    # round(..., 2) redondea el resultado a 2 decimales.
    # Si la lista está vacía, la media será 0 (evita división por cero).

    minima = min(notas) if total > 0 else None  
    # Obtiene la nota mínima si hay elementos, de lo contrario devuelve None.

    maxima = max(notas) if total > 0 else None  
    # Obtiene la nota máxima si hay elementos, de lo contrario devuelve None.

    return total, media, minima, maxima  
    # Devuelve los 4 resultados como una tupla (varios valores a la vez).

def porcentaje_aprobados(notas):
    """
    Calcula los porcentajes de:
    - Aprobados (nota >= 5)
    - Sobresalientes (nota >= 9)
    - Necesita Refuerzo (nota < 5)
    """

    total = len(notas)  # Cuenta cuántas notas hay en total.

    aprobados = sum(1 for n in notas if n >= 5)  
    # Suma 1 por cada nota que sea mayor o igual a 5 (aprobados).

    sobresalientes = sum(1 for n in notas if n >= 9)  
    # Suma 1 por cada nota que sea mayor o igual a 9 (sobresalientes).

    necesita_refuerzo = sum(1 for n in notas if n < 5)  
    # Suma 1 por cada nota que sea menor a 5 (necesitan refuerzo).

    return {
        "Aprobados": (aprobados / total * 100) if total > 0 else 0,  
        # Calcula el porcentaje de aprobados sobre el total; evita división por cero.

        "Sobresalientes": (sobresalientes / total * 100) if total > 0 else 0,  
        # Calcula el porcentaje de sobresalientes sobre el total; evita división por cero.

        "Necesita Refuerzo": (necesita_refuerzo / total * 100) if total > 0 else 0  
        # Calcula el porcentaje que necesita refuerzo; evita división por cero.
    }


def moda(notas):
    """
    Calcula la(s) moda(s): nota(s) más frecuente(s) entre las calificaciones.
    Si hay empate, muestra todas.
    """

    if not notas:
        return []  
        # Si la lista de notas está vacía, devuelve una lista vacía porque no hay moda.

    contador = Counter(notas)  
    # Cuenta cuántas veces aparece cada nota en la lista usando Counter.

    max_frecuencia = max(contador.values())  
    # Obtiene la frecuencia máxima (el número de veces que se repite la nota más común).

    modas = [nota for nota, freq in contador.items() if freq == max_frecuencia]  
    # Crea una lista con todas las notas que tienen esa frecuencia máxima, es decir, las más repetidas.

    return modas  
    # Devuelve la lista de moda(s).


def main():

    """
    Función principal que organiza la ejecución del programa.
    """
    
    notas = pedir_notas()

    if not notas:
        print("No se ingresaron calificaciones válidas. Programa terminado.")
        return

    total, media, minima, maxima = resumen_estadistico(notas)
    porcentajes = porcentaje_aprobados(notas)
    modas = moda(notas)

    # Mostrar los resultados
    print("\n--- Boletín de Aula ---")
    print(f"Número total de notas: {total}")
    print(f"Media: {media:.2f}")
    print(f"Nota mínima: {minima}")
    print(f"Nota máxima: {maxima}")
    print(f"Porcentaje de aprobados: {porcentajes['Aprobados']:.2f}%")
    print(f"Porcentaje de sobresalientes: {porcentajes['Sobresalientes']:.2f}%")
    print(f"Porcentaje de Necesita Refuerzo: {porcentajes['Necesita Refuerzo']:.2f}%")
    print(f"Moda(s): {', '.join(str(m) for m in modas)}")
    # print() muestra en pantalla el texto formateado con f-string
    
    # Dentro del f-string, se construye una cadena con:
    # ', '.join(...) -> une elementos con ", " como separador
    
    # (str(m) for m in modas) -> genera cada elemento de modas convertido a cadena (str)
    
    # Por ejemplo, si modas = [5, 7, 9], se genera: "5", "7", "9"
    
    # Luego ', '.join(...) une esos strings en: "5, 7, 9"
    
    # El resultado final que se imprime es:
    # Moda(s): 5, 7, 9
    

if __name__ == "__main__":  
    # comprueba si el archivo se está ejecutando directamente
    main()  
    # Si el archivo se está ejecutando directamente, llama a la función principal 'main()',
    # que inicia todo el programa.

