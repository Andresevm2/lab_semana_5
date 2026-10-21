def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)

def encontrar_maximo(lista_notas):
    if not lista_notas:
        return None
    return max(lista_notas)