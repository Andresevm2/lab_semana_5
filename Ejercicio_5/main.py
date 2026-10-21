import auth
import operaciones2
def ejecutar_cajero():
    saldo = 1000.0
    pin_correcto = "1234"

    print("=== CAJERO AUTOMÁTICO ===")

    if auth.verificar_pin(pin_correcto):
        while True:
            print("\n1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")

            opcion = input("Elija una opción: ")

            match opcion:
                case "1":
                    operaciones2.consultar_saldo(saldo)

                case "2":
                    try:
                        monto = float(input("Ingrese monto a depositar: "))
                        saldo = operaciones2.depositar(saldo, monto)
                    except ValueError:
                        print("Error: Debe ingresar un valor numérico.")

                case "3":
                    try:
                        monto = float(input("Ingrese monto a retirar: "))
                        saldo = operaciones2.retirar(saldo, monto)
                    except ValueError:
                        print("Error: Debe ingresar un valor numérico.")

                case "4":
                    print("Gracias por usar el cajero.")
                    break

                case _:
                    print("Opción inválida.")
    else:
        print("Tarjeta bloqueada por seguridad.")


if __name__ == "__main__":
    ejecutar_cajero()