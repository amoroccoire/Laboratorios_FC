import numpy as np
import matplotlib.pyplot as plt

def entrada():
    while True:
        try:
            filas = int(input("Ingrese la cantidad de filas: "))
            columnas = int(input("Ingrese la cantidad de columnas: "))
            return [filas, columnas]
        except ValueError:
            print("Ingrese un número válido.")

def apply_rule(rule, state, pos):
    left = state[pos - 1]
    center = state[pos]
    right = state[(pos + 1) % len(state)]
    index = (left << 2) | (center << 1) | right
    return rule[index]

def evolve(rule, initial_state, steps):
    state = initial_state.copy()
    history = [state.copy()]

    for _ in range(steps):
        new_state = np.zeros_like(state)
        for i in range(len(state)):
            new_state[i] = apply_rule(rule, state, i)
        state = new_state
        history.append(state.copy())
    
    return history

def plot_evolution(history):
    plt.figure(figsize=(10, 5))
    plt.imshow(history, cmap="binary", interpolation="nearest")
    plt.xlabel("Time Step")
    plt.ylabel("Cell")
    plt.title("Rule 30 Cellular Automaton Evolution")
    plt.show()

def main():
    # Definir salidas de la regla
    rule = np.array([0, 1, 1, 1, 1, 0, 0, 0], dtype=int)
    
    while True:
        try:
            opcion = int(input("[1] INICIAR\n[2] SALIR\nOPCION: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 2:
            print("Saliendo...")
            break
        elif opcion == 1:
            arr = entrada()
            filas = arr[0]
            columnas = arr[1]
            # Estado inicial
            initial_state = np.zeros(columnas, dtype=int)
            value = np.random.randint(low=0, high=columnas)
            initial_state[value] = 1
            # Evolve and plot
            steps = filas
            evolution_history = evolve(rule, initial_state, steps)
            plot_evolution(np.array(evolution_history))
        else:
            print("Opción no válida. Intente nuevamente.")

main()
