from .operaciones import calcular_promedio, encontrar_maximo

def generar_resumen(lista_notas):
    promedio = calcular_promedio(lista_notas)
    nota_maxima = encontrar_maximo(lista_notas)
    
    print("\n--- REPORTE DE NOTAS ---")
    print(f"Notas registradas: {lista_notas}")
    print(f"Promedio general:  {promedio:.2f}")
    print(f"Nota más alta:     {nota_maxima}")
    print("------------------------\n")