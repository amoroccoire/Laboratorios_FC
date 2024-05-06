import numpy as np
import matplotlib.pyplot as plt

def grafica(vi, a, t):
    #formula: vf = vi + a*t
    tiempo = np.linspace(0, t, num=200)
    velocidad = vi + a*tiempo

    plt.figure(figsize=(8,5))
    plt.plot(tiempo, velocidad, label="Velocidad - Tiempo")
    plt.title("Variacion de la velocidad respecto al tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.grid(True)
    plt.legend()
    plt.show()

def fuerza(m, vf, vi, t):
    a = (vf - vi)/t
    F = m * a
    return F, a

def datos():
    print("Ingrese los datos:\n")
    try:
        masa = float(input("MASA: "))
        vi = float(input("Velocidad Inicial: "))
        vf = float(input("Velocidad Final: "))
        t = float(input("Tiempo: "))
    except:
        print("\nIngrese solo numeros y todos los solicitados")
        return False

    if (masa <= 0 or t <= 0):
        print("Verifique los datos, masa > 0 y tiempo > 0")
        return False

    return [masa, vi, vf, t]

def main(): 
    while(True):
        opcion = input("\n[1] Iniciar\n[2] Salir\nOPCION: ")
        match(opcion):
            case '1':
                values = datos()
                if (values is False):
                    print("Intentelo de nuevo")
                else:
                    m, vi, vf, t = values
                    F, a = fuerza(m, vf, vi, t)
                    print("Fuerza descrita por el movil:", F, "N")
                    grafica(vi, a, t)
            case '2':
                break
            case _:
                print("Opcion incorrecta. Intentelo de nuevo")

main()

