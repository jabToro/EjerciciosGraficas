import matplotlib.pyplot as plt

# Ejercicio 2
fig, ax = plt.subplots()
cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]
# Define los datos para las barras
bars = ax.bar(cursos, cantidad, color='salmon')

# Titulo del gráfico
plt.title("Cantidad de cursos", fontweight="bold")

# Añadir etiquetas a las barras
ax.bar_label(bars, padding=3)

# Etiquetas de los ejes
ax.set_xlabel("cursos", fontweight="bold")
ax.set_ylabel("cantidad", fontweight="bold")
plt.savefig('Graficas/2.jpg')
plt.show()
