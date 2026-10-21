def consultar_saldo(saldo):
    """Muestra el saldo actual del usuario."""
    print(f"Su saldo actual es: ${saldo:.2f}")


def depositar(saldo, monto):
    """
    Realiza un depósito sumando el monto al saldo si es válido (> 0).
    Retorna el nuevo saldo actualizado.
    """
    if monto > 0:
        nuevo_saldo = saldo + monto
        print(f"Depósito exitoso. Nuevo saldo: ${nuevo_saldo:.2f}")
        return nuevo_saldo
    else:
        print("Monto inválido.")
        return saldo


def retirar(saldo, monto):
    """
    Realiza un retiro restando el monto si hay fondos suficientes y el monto es válido.
    Retorna el nuevo saldo si es posible, o el saldo original si falla.
    """
    if 0 < monto <= saldo:
        nuevo_saldo = saldo - monto
        print(f"Retiro exitoso. Nuevo saldo: ${nuevo_saldo:.2f}")
        return nuevo_saldo
    elif monto > saldo:
        print("Fondos insuficientes.")
        return saldo
    else:
        print("Monto inválido.")
        return saldo