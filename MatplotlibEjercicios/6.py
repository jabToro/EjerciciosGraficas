import matplotlib.pyplot as plt
import numpy as np

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(10, 6))  # Tamaño de la figura

# Generar datos: x entre 0 y 2π (con 1000 puntos para suavidad)
x = np.linspace(0, 2*np.pi, 1000)  # np.pi = π (3.1416...)
y_sin = np.sin(x)  # Función seno
y_cos = np.cos(x)  # Función coseno

# Dibujar ambas funciones
ax.plot(x, y_sin, color='blue', linewidth=2, label='sin(x)')
ax.plot(x, y_cos, color='red', linewidth=2, label='cos(x)')

# Personalización
ax.set_title("Funciones Seno y Coseno (0 a 2π)", fontsize=14, pad=20)
ax.set_xlabel("x (radianes)", fontsize=12)
ax.set_ylabel("Valor", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)  # Cuadrícula punteada

# Ejes y marcas personalizadas
ax.axhline(0, color='black', linewidth=0.8)  # Línea horizontal en y=0
ax.axvline(0, color='black', linewidth=0.8)  # Línea vertical en x=0
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])  # Marcas en el eje X
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])  # Etiquetas en π

# Leyenda y ajustes finales
ax.legend(fontsize=12, loc='upper right')
plt.tight_layout()  # Evita superposiciones
plt.savefig('Graficas/6.jpg')
plt.show()