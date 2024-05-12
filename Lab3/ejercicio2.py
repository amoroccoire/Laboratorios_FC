import numpy as np
import matplotlib.pyplot as plt

# Definir las cargas puntuales como una lista de tuplas (x, y, carga)
cargas = [(-2, 0, -5), ((3, 1, 3))]

# Definir los límites del plano
x_min, y_min = -5, -5 
x_max, y_max = 5, 5

# Resolución de la malla
resolucion = 10

# Calcular el número de puntos en la malla
filas, columnas = resolucion * (y_max - y_min), resolucion * (x_max - x_min)

# Generar la malla de puntos en el plano
coord_x, coord_y = np.linspace(x_min, x_max, columnas), np.linspace(y_min, y_max, filas)
malla_x, malla_y = np.meshgrid(coord_x, coord_y)

# Inicializar los componentes del campo eléctrico en cero
campo_ex = np.zeros((filas, columnas))
campo_ey = np.zeros((filas, columnas))

# Constante de Coulomb
k = 9 * 10**9

# Calcular el campo eléctrico en cada punto de la malla
for j in range(filas):
    for i in range(columnas):
        punto_x, punto_y = malla_x[j][i], malla_y[j][i]
        for carga in cargas:
            delta_x = punto_x - carga[0]
            delta_y = punto_y - carga[1]
 
            distancia = (delta_x**2 + delta_y**2)**0.5
 
            campo_electrico = (k * carga[2]) / (distancia**2)     
            campo_ex[j][i] += campo_electrico * (delta_x / distancia)
            campo_ey[j][i] += campo_electrico * (delta_y / distancia) 
             
# Crear la visualización del campo eléctrico
fig, ax = plt.subplots()
ax.set_aspect('equal')
#Representación de las cargas (circulares y rojas)
ax.scatter([carga[0] for carga in cargas], [carga[1] for carga in cargas], c='red', s=[abs(carga[2])*50 for carga in cargas], zorder=1)
for carga in cargas: #para las etiquetas de la cargas
    ax.text(carga[0]-0.4, carga[1]-0.8, '{} unit'.format(carga[2]), color='black', zorder=2)
#Dibujo de las lineas del campo eléctrico
ax.streamplot(coord_x, coord_y, campo_ex, campo_ey, linewidth=1, density=1.5, zorder=0)
 
plt.title('Simulación del Campo Eléctrico')
plt.show()
