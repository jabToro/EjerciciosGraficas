import pandas as pd
# Importar la biblioteca matplotlib (específicamente el módulo pyplot, alias 'plt')
import matplotlib.pyplot as plt
# Importar numpy para generar datos de ejemplo (opcional, pero útil)
import numpy as np

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

