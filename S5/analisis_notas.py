from collections import Counter  # Importa Counter para contar frecuencia de calificaciones.

def pedir_notas():
    
    #Solicita al usuario una lista de calificaciones separadas por comas.
    #Valida cada entrada y solo acepta valores numéricos válidos entre 0 y 10.
    
    notas = []
    notas_str = input("Introduce las calificaciones separadas por comas: ")
    partes = notas_str.split(",")

    for parte in partes:
        nota_limpia = parte.strip()
        if nota_limpia:
            try:
                nota = float(nota_limpia)
                if 0 <= nota <= 10:
                    notas.append(nota)
                else:
                    print(f"Nota fuera de rango (0-10): '{nota_limpia}' → Ignorada.")
            except ValueError:
                print(f"Entrada inválida: '{nota_limpia}' no es un número → Ignorada.")
    return notas

def resumen_estadistico(notas):
    #Calcula un resumen estadístico de las calificaciones: total, media, mínima y máxima.

    total = len(notas)
    media = round(sum(notas) / total, 2) if total > 0 else 0
    minima = min(notas) if total > 0 else None
    maxima = max(notas) if total > 0 else None
    return total, media, minima, maxima

def porcentaje_aprobados(notas):
    """
    Calcula los porcentajes de:
    - Aprobados (nota >= 5)
    - Sobresalientes (nota >= 9)
    - Necesita Refuerzo (nota < 5)
    """
    total = len(notas)
    aprobados = sum(1 for n in notas if n >= 5)
    sobresalientes = sum(1 for n in notas if n >= 9)
    necesita_refuerzo = sum(1 for n in notas if n < 5)
    return {
        "Aprobados": (aprobados / total * 100) if total > 0 else 0,
        "Sobresalientes": (sobresalientes / total * 100) if total > 0 else 0,
        "Necesita Refuerzo": (necesita_refuerzo / total * 100) if total > 0 else 0
    }

def moda(notas):
    """
    Calcula la(s) moda(s): nota(s) más frecuente(s) entre las calificaciones.
    Si hay empate, muestra todas.
    """
    if not notas:
        return []
    contador = Counter(notas)
    max_frecuencia = max(contador.values())
    modas = [nota for nota, freq in contador.items() if freq == max_frecuencia]  # Crea una lista con las notas que tienen la frecuencia máxima (es decir, las más repetidas).               
    return modas

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

if __name__ == "__main__":
    main()
