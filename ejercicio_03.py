"""
EJERCICIO 03: Día del año.

1. Haga una función que dado un mes (en número), retorne la cantidad de días que tiene el mes (considere febrero con 28 días)
2. Haga otra función que dado un mes y el día actual del mes (ambos en número), calcule la cantidad de días que van del año
3. Pídale al usuario que ingrese el mes actual (en número). Debe validar el dato ingresado.
4. Pídale al usuario que ingrese el día actual (en número). Debe validar el dato ingresado y debe tener coherencia con el mes
   indicado en el paso anterior. Por ejemplo, abril no puede tener 31 días.
5. Calcule el día presente del año según los datos ingresados por el usuario, utilizando las funciones que acaba de implementar
6. Muestre en pantalla el resultado

"""

def dias_del_mes(mes):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 28
    else:
        return 0

def dias_transcurridos(mes, dia):
    dias_acumulados = 0
    for m in range(1, mes):
        dias_acumulados += dias_del_mes(m)
    
    dias_acumulados += dia
    return dias_acumulados

mes_usuario = 0
while True:
    try:
        mes_usuario = int(input("Ingrese el número del mes actual (1 - 12): "))
        if 1 <= mes_usuario <= 12:
            break
        else:
            print("Mes inválido. Debe ingresar un número entre 1 y 12.")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

max_dias = dias_del_mes(mes_usuario)
dia_usuario = 0

while True:
    try:
        dia_usuario = int(input(f"Ingrese el día actual (1 - {max_dias}): "))
        if 1 <= dia_usuario <= max_dias:
            break
        else:
            print(f"Día inválido. El mes {mes_usuario} tiene entre 1 y {max_dias} días.")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

dia_del_año = dias_transcurridos(mes_usuario, dia_usuario)

print("\n--- RESULTADO ---")
print(f"Para la fecha {dia_usuario}/{mes_usuario}, han transcurrido {dia_del_año} días del año.")