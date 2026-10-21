def verificar_pin(pin_correcto, intentos_maximos=3):
    
    intentos = intentos_maximos
    
    while intentos > 0:
        pin_ingresado = input("Ingrese su PIN de 4 dígitos: ")
        if pin_ingresado == pin_correcto:
            return True
        else:
            intentos -= 1
            print(f"PIN incorrecto. Te quedan {intentos} intentos.")
            
    return False