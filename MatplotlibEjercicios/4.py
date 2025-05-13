import matplotlib.pyplot as plt   
import numpy as np                                

fig, ax = plt.subplots(1, 2)

# Subgráfico 1: Gráfico de línea
ax[0].plot(5, 2, label='Linea senoidal', linestyle='--')
ax[0].legend()

# Subgráfico 2: Histograma
data = np.random.randn(1000)
ax[1].hist(data, bins=30, alpha=0.5, label='Función cuadratica' , color='orange')

plt.show()