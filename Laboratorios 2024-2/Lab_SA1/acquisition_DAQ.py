'''
    Análisis de Señales 
    2024-2
    Universidad Tecnológica de Pereira
    Laboratorio 1: Adquisición y muestreo de señales
'''

# Importar librerías
import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
import matplotlib.pyplot as plt
import numpy as np

# Parámetros de adquisición
f_daq = 5000  
f_sam = 10    

# Adquisición y muestreo de señales
def new_func(f_daq, f_sam):
    '''
    Función para adquirir y muestrear una señal.
    f_daq: Frecuencia de muestreo original
    f_sam: Frecuencia de muestreo de la señal

    return: data, time, datam, timem
    '''
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("myDAQ1/ai0")
        task.timing.cfg_samp_clk_timing(f_daq, sample_mode=AcquisitionType.FINITE, samps_per_chan=5000)
        data = task.read(READ_ALL_AVAILABLE)
    data = np.array(data)
    time = np.arange(0, len(data) / f_daq, 1 / f_daq)
    factor = int(f_daq / f_sam)
    datam = data[::factor]
    timem = time[::factor]

    return data, time, datam, timem

# Subplot 1: Señal original y muestreada
plt.figure(figsize=[10, 4])
data, time, datam, timem = new_func(f_daq, f_sam)
plt.subplot(111)
plt.plot(time, data, label='Datos original', c='blue')
plt.stem(timem, datam, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
plt.xlabel('Tiempo (s)')
plt.legend(loc='upper right')
plt.title('Señal original y muestreada')
plt.show()

# Subplot 2: Primer aliasing
plt.figure(figsize=[10, 4])
data_alias1, time_alias1, datam_alias1, timem_alias1 = new_func(f_daq, f_sam)
plt.subplot(111)
plt.plot(time_alias1, data_alias1, label='Datos origial', c='blue')
plt.stem(timem_alias1, datam_alias1, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
plt.xlabel('Tiempo (s)')
plt.legend(loc='upper right')
plt.title('Primer aliasing')
plt.show()

# Subplot 3: Segundo aliasing
plt.figure(figsize=[10, 4])
data_alias2, time_alias2, datam_alias2, timem_alias2 = new_func(f_daq, f_sam)
plt.subplot(111)
plt.plot(time_alias2, data_alias2, label='Datos original', c='blue')
plt.stem(timem_alias2, datam_alias2, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
plt.xlabel('Tiempo (s)')
plt.legend(loc='upper right')
plt.title('Segundo aliasing')
plt.show()