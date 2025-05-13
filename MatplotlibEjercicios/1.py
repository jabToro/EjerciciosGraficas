import pandas as pd
# Importar la biblioteca matplotlib (específicamente el módulo pyplot, alias 'plt')
import matplotlib.pyplot as plt
# Importar numpy para generar datos de ejemplo (opcional, pero útil)
import numpy as np
""" 
# --- Configuración inicial del gráfico ---
# Crear una nueva figura con un tamaño específico (ancho, alto en pulgadas)
plt.figure(figsize=(10, 5))  # 10 pulgadas de ancho, 5 de alto

# --- Generar datos de ejemplo ---
# Crear un array de 100 puntos entre 0 y 10 para el eje X
x = np.linspace(0, 10, 100)
# Calcular los valores correspondientes en el eje Y (usando la función seno)
y = np.sin(x)

# --- Crear el gráfico de líneas ---
# Dibujar una línea con los datos x e y, y personalizarla:
# - 'label': Etiqueta para la leyenda.
# - 'color': Color de la línea (azul).
# - 'linestyle': Estilo de línea (continua en este caso).
# - 'linewidth': Grosor de la línea (2 píxeles).
plt.plot(x, y, label='sen(x)', color='blue', linestyle='--', linewidth=2)

# --- Personalización del gráfico ---
# Añadir un título al gráfico
plt.title("Gráfico de la Función Seno")
# Etiqueta para el eje X (con tamaño de fuente personalizado)
plt.xlabel("Ángulo (radianes)", fontsize=12)
# Etiqueta para el eje Y
plt.ylabel("Amplitud", fontsize=12)
# Añadir una cuadrícula al gráfico (de color gris claro y estilo punteado)
plt.grid(color='gray', linestyle=':', linewidth=0.5)
# Mostrar la leyenda (usando las etiquetas definidas en plt.plot())
plt.legend()

# --- Ajustes adicionales ---
# Establecer los límites del eje X (opcional)
plt.xlim(0, 10)
# Establecer los límites del eje Y (opcional)
plt.ylim(-1.5, 1.5)
# Añadir anotaciones en un punto específico (texto en x=5, y=0)
plt.text(5, 0, "Máximo local", fontsize=10, color='red')

# --- Guardar y mostrar ---
# Guardar el gráfico como imagen PNG (con alta resolución, 300 DPI)
plt.savefig('grafico_seno.png', dpi=300, bbox_inches='tight')
# Mostrar el gráfico en una ventana emergente
plt.show() """

# Ejercicio 1
fig, ax = plt.subplots()

_ = ax.plot([3, 7, 1, 5, 12], 'bs-', label='Linea simple')
_ = ax.legend(frameon=False, loc=0, title='Ejercicio 1')

# Set axis labels, display in bold
plt.grid(True)
ax.set_xlabel("Valores", fontweight="bold")
ax.set_ylabel("Y", fontweight="bold")
plt.savefig('Graficas/1.jpg')
plt.show()

