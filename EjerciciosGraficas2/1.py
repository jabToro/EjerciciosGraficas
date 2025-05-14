import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuración básica
fig, ax = plt.subplots()
ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

# Datos estáticos
x = np.linspace(0, 4*np.pi, 200)

# Función de inicialización
def init():
    line.set_data([], [])
    return line,

# Función de actualización por frame
def update(t):
    y = np.sin(x + t)  # Desplazamiento de fase
    line.set_data(x, y)
    return line,

# Crear animación
ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 2*np.pi, 100),
    init_func=init,
    blit=True,
    interval=30
)
ani.save("GraficasAnimadas/1.gif", writer="pillow", fps=5)
plt.show()