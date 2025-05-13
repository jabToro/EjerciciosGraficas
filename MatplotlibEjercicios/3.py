import random
import matplotlib.pyplot as plt

listaAleat = [random.randint(1, 100) for _ in range(50)]
listaAleat2 = [random.randint(50, 150) for _ in range(50)]

fig, ax = plt.subplots()

_ = ax.scatter(listaAleat, listaAleat2, color='green', s=24, label='Dispersión')
_ = ax.legend(frameon=False, loc='upper right', title='Ejercico 3')

# Set axis labels, display in bold
ax.set_xlabel("valores", fontweight="bold")
ax.set_ylabel("Valores", fontweight="bold")
plt.savefig('Graficas/3.jpg')
plt.show()
