from collections import Counter                                                     # Importa la clase Counter del módulo collections para contar frecuencias de elementos.

def pedir_notas():                                                                  # Solicita al usuario una lista de calificaciones,
    notas_str = input("Introduce las calificaciones separadas por comas: ")
    partes = notas_str.split(",")                                                   # Paso 2: Dividir la cadena en partes usando la coma como separador
    notas = []                                                                      # Paso 3: Inicializar una lista vacía para almacenar las calificaciones
    for parte in partes:                                                            # Paso 4: Recorrer cada parte de la lista original
        nota_limpia = parte.strip()                   
                                      
        if nota_limpia:                                                             # Verificar que no esté vacía (por si el usuario puso comas de más)
            notas.append(float(nota_limpia))                                        # Convertir a número decimal (float) y agregarlo a la lista de notas
    return notas

def resumen_estadistico(notas):                                                     # Calcula un resumen estadístico de las calificaciones: total, media, mínima y máxima.
    total = len(notas)                                                                  # Número total de calificaciones.
    media = sum(notas) / total if total > 0 else 0                                  # Media aritmética.
    minima = min(notas) if total > 0 else None                                          # Nota mínima.
    maxima = max(notas) if total > 0 else None                                      # Nota máxima.
    return total, media, minima, maxima

def porcentaje_aprobados(notas):                                                    # Calcula el porcentaje de aprobados, sobresalientes y estudiantes que necesitan refuerzo.
    aprobados = sum(1 for n in notas if n >= 5)                                         # Calificaciones mayores o iguales a 5.
    sobresalientes = sum(1 for n in notas if n >= 9)                                # Calificaciones mayores o iguales a 9.
    necesita_refuerzo = sum(1 for n in notas if n < 5)                                  # Calificaciones menores a 5.
    total = len(notas)                                                              # Total de calificaciones.
    return {
        "Aprobados": (aprobados / total * 100) if total > 0 else 0,
        "Sobresalientes": (sobresalientes / total * 100) if total > 0 else 0,
        "Necesita Refuerzo": (necesita_refuerzo / total * 100) if total > 0 else 0
    }

def moda(notas):                                                                    # Calcula la moda (o modas) de las calificaciones, es decir, las más frecuentes.
    contador = Counter(notas)                                                           # Cuenta la frecuencia de cada calificación.
    max_frecuencia = max(contador.values())                                         # Encuentra la frecuencia máxima.
    modas = [nota for nota, freq in contador.items() if freq == max_frecuencia]         # Notas con frecuencia máxima.
    return modas

def main():                                                                         # Función principal que coordina la ejecución del programa.
    notas = pedir_notas()                                                               # Solicita las calificaciones al usuario.
    total, media, minima, maxima = resumen_estadistico(notas)                       # Calcula el resumen estadístico.
    porcentajes = porcentaje_aprobados(notas)                                           # Calcula los porcentajes de aprobados, sobresalientes y refuerzo.
    modas = moda(notas)                                                             # Calcula la moda de las calificaciones.

    print("\n--- Boletín de Aula ---")                                              # Imprime el boletín con los resultados.
    print(f"Número total de notas: {total}")
    print(f"Media: {media:.2f}")
    print(f"Nota mínima: {minima}")
    print(f"Nota máxima: {maxima}")
    print(f"Porcentaje de aprobados: {porcentajes['Aprobados']:.2f}%")
    print(f"Porcentaje de sobresalientes: {porcentajes['Sobresalientes']:.2f}%")
    print(f"Porcentaje de Necesita Refuerzo: {porcentajes['Necesita Refuerzo']:.2f}%")
    print(f"Moda(s): {', '.join(str(m) for m in modas)}")

if __name__ == "__main__":                                                          # Ejecuta la función principal solo si el archivo se ejecuta directamente.
    main()