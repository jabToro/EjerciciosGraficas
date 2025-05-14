import numpy as np
import matplotlib.pyplot as plt

# Configuración
plt.figure(figsize=(10, 6))

# Generar datos
datos = np.random.normal(loc=0, scale=1, size=1000)  # media=0, desviación=1

# Crear histograma (guardando los valores de retorno para usar 'density')
n, bins, patches = plt.hist(datos, 
                           bins=30,
                           color='skyblue',
                           edgecolor='black',
                           alpha=0.7,
                           density=True)  # Normalizado a densidad

# Personalización
plt.title('Histograma de Distribución Normal (1000 puntos)', fontsize=14)
plt.xlabel('Valor', fontsize=12)
plt.ylabel('Densidad de Probabilidad' if density else 'Frecuencia', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.legend()
plt.tight_layout()
plt.show()