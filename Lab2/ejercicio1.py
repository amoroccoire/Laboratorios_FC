def getTension(aceleracion, masa):
    gravedad = 9.8
    tension = masa * (aceleracion + gravedad)
    return tension

def getAceleracion(masa1, masa2):
    gravedad = 9.8
    aceleracion = gravedad * (masa1 - masa2)/(masa1 + masa2)
    return aceleracion

def maquinaAtwood():
    masa1 = float(input("Ingrese la masa 1: "))
    masa2 = float(input("Ingrese al masa 2: "))

    if (masa1 < 0 or masa2 < 0):
        print("Las masas no pueden ser negativas")
        return False
    elif ((masa1 + masa2) == 0):
        print("Las masas no pueden sumar 0")
        return False

    aceleracion = 0
    tension = None
    if (masa1 > masa2):
        aceleracion = getAceleracion(masa1, masa2)
        tension = getTension(aceleracion, masa1)      
    elif (masa1 < masa2):
        aceleracion = getAceleracion(masa2, masa1)
        tension = getTension(aceleracion, masa2)
    else:
        tension = getTension(aceleracion, masa1)
    
    print("La aceleración del sistema es:", aceleracion, "m/s^2")
    print("La tensión de la cuerda es:", tension, "N")

def main():
    while(True):
        opcion = input("\n[1] Iniciar\n[2] Salir\nOPCION: ")
        match(opcion):
            case '1': 
                e = maquinaAtwood()
                if (e is False):
                    print("\nIntentelo de nuevo")
            case '2':
                break
            case _:
                print("Opcion incorrecta. Intentelo de nuevo")
    print("\nBye")

main()
