import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n_puntos = 50
# Usar listas mutables para x e y
x = list(np.random.rand(n_puntos) * 10)
y = list(np.random.rand(n_puntos) * 10)

fig, ax = plt.subplots()
scat = ax.scatter(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def animate(frame):
    # Modificar las listas directamente
    for i in range(n_puntos):
        x[i] += np.random.normal(0, 0.1)
        y[i] += np.random.normal(0, 0.1)
    scat.set_offsets(np.c_[x, y])  # Correcto (array 2D)
    return scat,

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
ani.save("GraficasAnimadas/2.gif", writer="pillow", fps=5)
plt.show()