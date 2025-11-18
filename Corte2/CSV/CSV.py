import numpy as np # importar NumPy para generar números aleatorios
import matplotlib.pyplot as plt # importar pyplot de matplotlib para crear la figura y la gráfica
from matplotlib.animation import FuncAnimation # importar FuncAnimation para actualizar la gráfica en intervalos

N = 50 #Cantidad de datos que aparecen al mismo tiempo en la gráfica
x_data = list(range(N))  #Crea la lista del eje X
y_data = [0] * N  #Crea la lista del eje Y

fig, ax = plt.subplots()  # crea la figura (fig) y los ejes (ax)
line, = ax.plot(x_data, y_data) # dibuja la línea inicial y toma el primer elemento de la lista que devuelve para quedarnos solo con el objeto que representa la línea de la gráfica

ax.set_ylim(0, 10) # fija los límites verticales del eje Y entre 0 y 10
ax.set_title("Gráfica en tiempo real")   # establece el título de la gráfica
ax.set_xlabel("Tiempo") # etiqueta del eje X
ax.set_ylabel("Valor") # etiqueta del eje Y

def update(frame):                               # Función que actualiza los datos en cada fotograma/intervalo
    new_value = np.random.uniform(0, 10)         # Genera un nuevo valor aleatorio uniforme entre 0 y 10
    y_data.append(new_value)                     # Añade el nuevo valor al final de la lista y_data
    y_data.pop(0)                                # Elimina el primer (más antiguo) valor para mantener la longitud N
    line.set_ydata(y_data)                       # Actualiza los datos Y de la línea con la lista desplazada
    return line,                                 # Devuelve la línea en una tupla (requerido por FuncAnimation)

ani = FuncAnimation(fig, update, interval=200)  # Crea la animación llamando a update() cada 200 ms

plt.show()                                       # Muestra la ventana gráfica y arranca el bucle de actualización
