import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



# Crear datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear la figura y los ejes
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Dibujar la línea inicial
line, = ax.plot(x, y)

# Definir los límites de los sliders
axcolor = 'lightgoldenrodyellow'
axamp = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)

# Crear el slider
samp = Slider(axamp, 'Amplitud', 0.1, 10.0, valinit=1)

# Función para actualizar el gráfico cuando se cambia el valor del slider
def update(val):
    amp = samp.val
    line.set_ydata(np.sin(amp * x))
    fig.canvas.draw_idle()

# Conectar el slider con la función de actualización
samp.on_changed(update)

plt.show()
