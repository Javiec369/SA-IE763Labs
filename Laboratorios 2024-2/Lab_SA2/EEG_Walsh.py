'''
    Análisis de Señales
    2024-2
    Universidad Tecnológica de Pereira
    Laboratorio 2: Transformada de Walsh
'''

# Importar librerías
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd
from scipy.fft import fft
from scipy.linalg import hadamard
from sympy import fwht, ifwht

def w_func(y, n):
    '''
    Función que realiza la reconstrucción de una señal
    a partir de la transformada de Walsh-Hadamard

    Parámetros:
    y -- Señal a reconstruir
    n -- Número de componentes a utilizar

    Return:
    rec -- Señal reconstruida
    ''' 
    desc = fwht(y)
    desc[n:len(y)] = [0] * (len(y) - n)
    rec = ifwht(desc)
    return rec

# Visualización de la EEG original
'''Cargar datos con pandas (pd) una vez pasado el txt a un archivo Excel.
Modificar el número al final de 'EXGChannel' para seleccionar el canal deseado.
'''
data = pd.read_excel('ruta: se recomienda ruta relativa')
data = data.drop([0, 1, 2, 3]).reset_index(drop=True)
data = data.drop(data.columns[0], axis=1)
data = data.drop(data.columns[9:], axis=1)
data.columns = [f'EXGChannel{i}' for i in range(9)]
# Seleccionar el canal entre 0 y 8
ch = data['EXGChannel6']

# Acotar los datos de ese ch seleccionado a un número múltiplo de 2
ch_r = ch[:2**13]

N = len(ch_r)  # Número de muestras
F = 125        # Frecuencia de muestreo (Hz)
Ts = N / F
t = np.linspace(0, Ts, N)

fig, axs = plt.subplots(2, 1, figsize=(12, 6))
# Gráfica señal original
axs[0].plot(t, ch_r)
axs[0].set_title('Señal Original')
axs[0].set_ylabel('Amplitud')

'''A continuación, determine la cantidad de armónicos necesarios para reconstruir 
la señal. Considere una base de 2 para la reconstrucción.
'''
####Código------------------------------------------------- 
n = 0
####------------------------------------------------------
rec = w_func(ch_r, n)
signal_r = rec
# Gráfica señal reconstruida
axs[1].plot(t, signal_r, 'r', label=f'Reconstrucción con {n} componentes')
axs[1].set_title(f'Señal reconstruida a partir de {n} componentes')
axs[1].set_xlabel('Tiempo (s)')
axs[1].set_ylabel('Amplitud')
axs[1].legend(loc='best')

plt.show()

# Generación de la matriz de Hadamard y visualización
'''Genere un script para visualizar la matriz de Hadamard deacuerdo a un número 
arbitrario de componentes.
'''
####Código-------------------------------------------------
n = 0
####------------------------------------------------------
