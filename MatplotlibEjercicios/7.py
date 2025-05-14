import numpy as np
import matplotlib.pyplot as plt

# 1. Generar los vectores aleatorios
np.random.seed(42)  # Para reproducibilidad
vector1 = np.random.randint(0, 101, 100)
vector2 = np.random.randint(0, 101, 100)

# 2. Calcular las estadísticas
suma_total = np.sum(vector1) + np.sum(vector2)
maximo = max(np.max(vector1), np.max(vector2))
desviacion_std = (np.std(vector1), np.std(vector2))

# 3. Crear la figura con subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico 1: Distribución de los valores
ax1.hist(vector1, bins=20, alpha=0.7, label='Vector 1', color='blue')
ax1.hist(vector2, bins=20, alpha=0.7, label='Vector 2', color='orange')
ax1.set_title('Distribución de Valores')
ax1.set_xlabel('Valor')
ax1.set_ylabel('Frecuencia')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

# Gráfico 2: Resultados estadísticos
stats_labels = ['Suma Total', 'Valor Máximo', 'Desviación Estándar']
stats_values = [suma_total, maximo, desviacion_std[0]]  # Mostramos solo Vector1 para evitar duplicados

ax2.bar(stats_labels, stats_values, color=['green', 'red', 'purple'])
ax2.set_title('Estadísticas Clave')
ax2.set_ylabel('Valor')
ax2.grid(True, linestyle='--', alpha=0.6)

# Añadir texto con los resultados completos
stats_text = f"""
Estadísticas completas:
- Suma total: {suma_total}
- Máximo Vector 1: {np.max(vector1)}
- Máximo Vector 2: {np.max(vector2)}
- Desviación Vector 1: {desviacion_std[0]:.2f}
- Desviación Vector 2: {desviacion_std[1]:.2f}
"""
plt.figtext(0.5, -0.1, stats_text, ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.savefig('Graficas/7.jpg')
plt.show()