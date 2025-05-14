import matplotlib.pyplot as plt   
import numpy as np                                

import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))  # 1 fila, 2 columnas

# Datos para los gráficos
x = np.linspace(0, 10, 100)  # Eje X común (100 puntos entre 0 y 10)

# --- Subgráfico 1: Función senoidal (y = sin(x)) ---
y_sin = np.sin(x)
ax1.plot(x, y_sin, color='blue', linestyle='-', linewidth=2, label='sen(x)')
ax1.set_title("Función Senoidal", fontsize=12)
ax1.set_xlabel("Eje X", fontweight='bold')
ax1.set_ylabel("Amplitud", fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend()

# --- Subgráfico 2: Función cuadrática (y = x^2) ---
y_quad = x ** 2  # y = x²
ax2.plot(x, y_quad, color='red', linestyle='--', linewidth=2, label='x²')
ax2.set_title("Función Cuadrática", fontsize=12)
ax2.set_xlabel("Eje X", fontweight='bold')
ax2.set_ylabel("y = x²", fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend()

# Ajustar espacio entre subgráficos y mostrar
plt.tight_layout()
plt.savefig('Graficas/4.jpg')
plt.show()