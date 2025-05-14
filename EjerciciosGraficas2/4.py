import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


df = pd.read_csv('archivoPrueba.CSV')

# Lista de años ordenados
anios = sorted(df['Año'].unique())
paises = df['País'].unique()

fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    anio = anios[i]
    datos_anio = df[df['Año'] == anio]
    ax.bar(datos_anio['País'], datos_anio['Valor'], color='skyblue')
    ax.set_ylim(0, df['Valor'].max() * 1.1)
    ax.set_title(f'Evolución por país - Año {anio}')
    ax.set_ylabel('Valor')
    ax.set_xlabel('País')

ani = FuncAnimation(fig, animate, frames=len(anios), interval=800, repeat=True)

plt.tight_layout()
ani.save("GraficasAnimadas/4.gif", writer="pillow", fps=20)
plt.show()