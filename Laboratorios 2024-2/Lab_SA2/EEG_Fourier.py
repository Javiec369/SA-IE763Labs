'''
    Análisis de Señales
    2024-2
    Laboratorio 2: Transformada de Fourier
'''

# Importar librerías
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import pandas as pd

def f_series(t, F, n, y):
    '''
    Función que realiza la reconstrucción de una señal 
    a partir de series de Fourier

    Parámetros:
    t -- Vector de tiempo
    F -- Frecuencia de muestreo
    n -- Número de armónicos a utilizar
    y -- Señal a reconstruir

    Return:
    rec -- Señal reconstruida
    '''
    Y = fft(y)
    # rec = np.ones(len(t)) * (np.abs(Y[0])) / len(y)
    rec = np.zeros(np.size(t))
    
    for k in range(0, n + 1):
        An = 2 * np.abs(Y[k]) / len(Y)
        th = np.angle(Y[k])
        wn = 2 * np.pi * F * k
        rec += An * np.cos(wn * t + th)
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
ch = data['EXGChannel3']

# Acotar los datos de ese ch seleccionado a un número múltiplo de 2
ch_r = ch[:2**12]

N = len(ch_r)  # Número de muestras
F = 125        # Frecuencia de muestreo (Hz)
Ts = N / F
t = np.linspace(0, Ts, N)

# Gráfica señal original
plt.subplot(2, 1, 1)
plt.plot(t, ch_r)
plt.title('Señal Original')
plt.ylabel('Amplitud')

'''A continuación, determine la cantidad de armónicos necesarios para reconstruir 
la señal. Considere una base de 2 para la reconstrucción.
'''
####Código------------------------------------------------- 
n = 0
####------------------------------------------------------
rec = f_series(t, F, n, ch_r)  # Reconstrucción a partir de series de Fourier

# Gráfica señal reconstruida
plt.subplot(2, 1, 2)
plt.plot(t, rec, 'r', label=f'Reconstrucción con {n} armónicos')
plt.title(f'Señal reconstruida a partir de {n} armónicos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend(loc='best')

plt.show()

# Generación y visualización de la DFT
'''Genere un script para visualizar la matriz de la DFT de un tamaño de 2^k x 2^k.
'''
####Código-------------------------------------------------
k = 7
n = 2**k
####------------------------------------------------------