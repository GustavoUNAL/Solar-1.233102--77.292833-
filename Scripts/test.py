import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, FloatSlider

# Función para graficar y actualizar el gráfico
def plot_sine_wave(amplitude, frequency):
    x = np.linspace(0, 10, 100)
    y = amplitude * np.sin(frequency * x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('Gráfico de una onda seno')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Crear sliders interactivos para la amplitud y frecuencia
amplitude_slider = FloatSlider(value=1.0, min=0.1, max=2.0, step=0.1, description='Amplitud:')
frequency_slider = FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Frecuencia:')

# Crear la interfaz interactiva
interact(plot_sine_wave, amplitude=amplitude_slider, frequency=frequency_slider);
