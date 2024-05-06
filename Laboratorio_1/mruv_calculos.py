import math

def V_inicial(variables):
    Vf, Dx, Vi, Dt, alpha = variables
    
    if(Dt == 0):
        print("No es posible division por 0")
        return False
    if (Vf is False):
        return ((Dx / Dt) - (alpha*Dt/2))
    return ((Vf/Dt) - alpha)

def calcular_alpha(variables):
    Vf, Dx, Vi, Dt, alpha = variables
    
    if(Dt == 0):
        print("No es posible division por 0")
        return False

    if (Vf is False):
        return ((2*Dx/(Dt**2)) - (2*Vi/Dt))
    return ((Vf/Dt) - Vi)

def calcular_deltaT(variables):
    Vf, Dx, Vi, Dt, alpha = variables

    if (Vf == False):
        if (alpha == 0):
            print("Alpha debe ser distinto de 0")
            return False
        discriminante = Vi**2 + 2*alpha*Dx
        if (discriminante < 0):
            print("No existen soluciones reales para Delta_T")
            return False
        return (-Vi + math.sqrt(discriminante))/alpha
    elif ((Vi + alpha) == 0):
        print("La suma de Vi y alpha no puede ser 0")
        return False
    return Vf/(Vi + alpha)

def V_final(variables):
    Vf, Dx, Vi, Dt, alpha = variables
    return Dt*(Vi+alpha)

def calculo_deltaX(variables):
    Vf, Dx, Vi, Dt, alpha = variables
    return Vi*Dt + (alpha*(Dt**2)/2)

