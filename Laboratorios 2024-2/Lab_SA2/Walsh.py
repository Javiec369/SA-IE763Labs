import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.linalg import hadamard
from sympy import fwht, ifwht

# Cargar los datos desde un archivo Excel
data = pd.read_excel(r'C:\leydi\universidad\automatica\Practicas de señales\practicas20242\practica2\ejemplo.xlsx')
data = data.drop([0, 1, 2, 3]).reset_index(drop=True)
data = data.drop(data.columns[0], axis=1)
data = data.drop(data.columns[16:], axis=1)
data.columns = [f'EXGChannel{i}' for i in range(16)]

ch = data['EXGChannel5']

# Acotar los datos de ese ch seleccionado a un número múltiplo de 2
ch_r = ch[:2**12]

t = np.linspace(0, 10, len(ch_r))
m=8
n = 2**m  # Cantidad de componentes deseados para la reconstrucción

# Función para la reconstrucción usando transformada de Walsh-Hadamard
def w_func(y, n):
    desc = np.array(fwht(y), dtype=float)
    desc[n:] = 0
    rec = np.array(ifwht(desc), dtype=float)
    return rec

# Reconstrucción de la señal
rec = w_func(ch_r, n)
t_rec = np.linspace(0, 10, len(rec))

# Visualización de la señal original y la reconstruida
plt.figure()
plt.plot(t, ch_r, 'b', label='Señal original')
plt.plot(t_rec, rec, 'r', label=f'Reconstrucción con {n} componentes')
plt.title(f'Señal reconstruida a partir de {n} componentes')
plt.xlabel('Tiempo')
plt.ylabel('Voltaje')
plt.legend(loc='best')
plt.grid(True)
plt.show()



# Generación de la matriz de Hadamard y visualización
order = 32  # Orden de la matriz de Hadamard
H = hadamard(order)
plt.subplot(1, 1, 1)
plt.imshow(H, cmap='hot', interpolation='nearest')
plt.title('Heatmap de la matriz de Hadamard')
plt.show()