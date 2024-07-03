'''
    Análisis de Señales
    2024-2
    Laboratorio 2: 
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import pandas as pd

def f_series(t, F, n, y):
    Y = fft(y)
    rec = np.ones(len(t)) * (np.abs(Y[0])) / len(y)
    
    for k in range(1, n + 1):
        An = 2 * np.abs(Y[k]) / len(Y)
        th = np.angle(Y[k])
        wn = 2 * np.pi * F * k
        rec += An * np.cos(wn * t + th)
        
    rec=rec+2*(Y[0])/ len(y)
    return rec

# Cargar datos desde un archivo Excel
data = pd.read_excel(r'C:\leydi\universidad\automatica\Practicas de señales\practicas20242\practica2\ejemplo.xlsx')
data = data.drop([0, 1, 2, 3]).reset_index(drop=True)
data = data.drop(data.columns[0], axis=1)
data = data.drop(data.columns[16:], axis=1)
data.columns = [f'EXGChannel{i}' for i in range(16)]

# Elegir canal a representar
ch = data['EXGChannel5']

# Acotar los datos de ese ch seleccionado a un número múltiplo de 2
ch_r = ch[:2**13]

N = len(ch_r)  # Número de muestras
F = 125        # Frecuencia de muestreo (Hz)
Ts = N / F
t = np.linspace(0, Ts, N)

m=6 
n = 2**m # Cantidad de armónicos deseados para la reconstrucción
rec = f_series(t, F, n, ch_r)  # Reconstrucción a partir de series de Fourier

plt.figure()
plt.plot(t, ch_r, 'b', label='Señal original')
plt.plot(t, rec, 'r', label=f'Reconstrucción con {n} componentes')
plt.title(f'Señal reconstruida a partir de {n} componentes')
plt.xlabel('Tiempo')
plt.ylabel('Voltaje')
plt.legend(loc='best')
plt.grid(True)
plt.show()

plt.show()