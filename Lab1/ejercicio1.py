import mruv_calculos as mruvFunctions
import matplotlib.pyplot as plt
import numpy as np

def grafica(Vi, alpha, tiempo):
    t = np.linspace(0, tiempo, 300)
    delta_x = Vi*t + 0.5*alpha*t**2
    plt.figure(figsize=(8, 5))
    plt.plot(t, delta_x, label='Desplazamiento - Tiempo')
    plt.title('Desplazamiento como función del tiempo')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Desplazamiento (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

def ingresoDatos(etiquetas, variables):
    print("Presione enter para saltar la variable que no tenga valor\n")
    for i in range(0, len(variables)):
        temp = input(etiquetas[i] + ": ")
        try:
            variables[i] = float(temp)
        except:
            continue

def contadorDeFalsos(variables):
    count = 0
    for i in variables:
        if i is False:
            count = count + 1
    return count

def mru():
    etiquetas = ["Delta X (m)", "Delta T (s)", "Velocidad (m/s)"]
    variables = [False, False, False]

    #Ingreso de las variables
    ingresoDatos(etiquetas, variables)
    
    #Verificacion de la existencia de al menos 2 variables o si no hay nada que calcular (3 variables completas)
    count = contadorDeFalsos(variables)

    if (count == 0):
        print("Todos los datos estan completos\n")
        return False
    elif (count > 1):
        print("Es necesario que ingrese al menos 2 variables\n")
        return False
    
    Dx, Dt, V = variables
    if (Dt < 0):
        print("Delta_T no puede ser menor a 0")
        return False

    #Inicio de los calculos y verificaciones de division por 0
    if (Dx is False): #calculo de Delta X
        return (etiquetas[0], V*Dt, "m.")
    
    elif (Dt is False and V != 0): #calculo de Delta T
        return (etiquetas[1], Dx/V, "s.")
    
    elif (V is False and Dt != 0): #calculo velocidad
        return (etiquetas[2], Dx/Dt, "m/s")
    else:
        print("No es posible division por 0\n")
        return False

def mruv():
    etiquetas = ["Velocidad final (m/s)", "Delta X (m)", "Velocidad inicial (m/s)", "Delta T (s)", "Alpha (m/s^2)"]
    variables = [False, False, False, False, False]

    #Ingreso de las variables
    ingresoDatos(etiquetas, variables)
    
    #Si existen 5 o 4 variables, no se calcula nada
    count = contadorDeFalsos(variables)

    if (count < 1):
        print("\nLa mayoria de los datos estan completos, no es necesario iniciar calculos")
        return False
    elif (count > 2):
        print("Es necesario que ingrese al menos 3 variables\n")
        return False

    Vf, Dx, Vi, Dt, alpha = variables
    if (Dt < 0):
        print("Delta_T no puede ser menor a 0")
        return False
    
    if (Vi is False and Dt is not False and alpha is not False): #Velocidad inicial
        velocidad_inicial = mruvFunctions.V_inicial(variables)
        grafica(velocidad_inicial, alpha, Dt)
        return (etiquetas[2], velocidad_inicial, "m/s")
    elif (alpha is False and Dt is not False and Vi is not False): #alpha
        alpha_resultado = mruvFunctions.calcular_alpha(variables)
        grafica(Vi, alpha_resultado, Dt)
        return (etiquetas[4], alpha_resultado, "m/s^2")
    elif (Dt is False and Vi is not False and alpha is not False): #Delta_T
        deltaT_calculado = mruvFunctions.calcular_deltaT(variables)
        grafica(Vi, alpha, deltaT_calculado)
        return (etiquetas[3], deltaT_calculado, "s")
    elif (Vi is not False and Dt is not False and alpha is not False):
        grafica(Vi, alpha, Dt)
        if (Vf is False or Dx is False):
            return [
                (etiquetas[1], mruvFunctions.calculo_deltaX(variables), "m"), #DELTA_X
                (etiquetas[0], mruvFunctions.V_final(variables), "m/s") #Velocidad final
                ]
    else:
        print("Los datos ingresados no concuerdan con ninguna formula") 
        return False

while (True):
    opcion = int(input("[1] MRU\n[2] MRUV\n[3] Salir\nOPCION: "))

    match (opcion):
        case 1:
            dato = mru()
            if (dato is False):
                print("\nIntentelo de nuevo")
            else:
                print("\t", dato[0], "es:", dato[1], dato[2],"\n")
        case 2:
            print("Para ver la grafica debe incluir Vi y alpha")
            dato = mruv()
            if (isinstance(dato, list)):
                print("\t", dato[0][0], "es: ", dato[0][1], dato[0][2])
                print("\t", dato[1][0], "es: ", dato[1][1], dato[1][2])
            elif (dato is False or dato[1] is False):
                print("\nIntentelo de nuevo")
            else:
                print("\t", dato[0], "es:", dato[1], dato[2],"\n")
        case 3:
            break
        case _:
            print("Opcion incorrecta. Intentelo de nuevo")

print("\nBye")