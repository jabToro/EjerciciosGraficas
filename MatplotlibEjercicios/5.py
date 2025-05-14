import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
fig, ax = plt.subplots(figsize=(8, 5))  # Figura única

# Generar datos
x = np.linspace(-10, 10, 500)  # 500 puntos entre -10 y 10
y = x**2 - 3*x + 2  # Función cuadrática y = x² - 3x + 2

# Graficar
ax.plot(x, y, color='dodgerblue', linewidth=2.5, label=r'$y = x^2 - 3x + 2$')

# Personalización
ax.set_title("Función Cuadrática", fontsize=14, pad=20)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)

# Líneas horizontales/verticales y anotaciones
ax.axhline(0, color='black', linewidth=0.8)  # Eje X
ax.axvline(0, color='black', linewidth=0.8)  # Eje Y

ax.legend(fontsize=10)

# Mostrar
plt.tight_layout()
plt.savefig('Graficas/5.jpg')
plt.show()