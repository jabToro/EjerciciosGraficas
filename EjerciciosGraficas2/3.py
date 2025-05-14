import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros del círculo
n_puntos = 100
radio = 5
angulo = np.linspace(0, 2 * np.pi, n_puntos)
# Coordenadas iniciales
x = radio * np.cos(angulo)
y = radio * np.sin(angulo)
# Velocidad angular
velocidad_angular = 0.1
# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(-radio - 1, radio + 1)
ax.set_ylim(-radio - 1, radio + 1)
ax.set_aspect('equal')
ax.set_title("Círculo Girando")
ax.set_xlabel("X")
ax.set_ylabel("Y")
# Crear un punto en el círculo
punto, = ax.plot([], [], 'ro')
# Inicialización
def init():
    punto.set_data([], [])
    return punto,
# Función de actualización para cada frame
def update(frame):
    # Calcular nuevas coordenadas
    x_nuevo = radio * np.cos(angulo + velocidad_angular * frame)
    y_nuevo = radio * np.sin(angulo + velocidad_angular * frame)
    punto.set_data(x_nuevo, y_nuevo)
    return punto,
# Crear la animación
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)
# Guardar como GIF
ani.save("GraficasAnimadas/3.gif", writer="pillow", fps=20)
# Mostrar (opcional)
plt.show()