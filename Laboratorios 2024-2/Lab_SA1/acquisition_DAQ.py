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
def Acquisition_function(f_daq, f_sam):
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
    # Muestreo
    factor = int(f_daq / f_sam)
    data_m = data[::factor]
    time_m = time[::factor]

    return data, time, data_m, time_m

# Subplot 1: Señal original y muestreada
plt.figure(figsize=[10, 4])
data, t, data_m, t_m = Acquisition_function(f_daq, f_sam)
plt.subplot(111)
plt.plot(t, data, label='Datos original', c='blue')
plt.stem(t_m, data_m, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
plt.xlabel('Tiempo (s)')
plt.legend(loc='upper right')
plt.title('Señal original y muestreada')
plt.show()

# Subplot 2: Primer aliasing
plt.figure(figsize=[10, 4])
data_alias1, t_alias1, datam_alias1, tm_alias1 = Acquisition_function(f_daq, f_sam)
plt.subplot(111)
plt.plot(t_alias1, data_alias1, label='Datos origial', c='blue')
plt.stem(tm_alias1, datam_alias1, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
plt.xlabel('Tiempo (s)')
plt.legend(loc='upper right')
plt.title('Primer aliasing')
plt.show()

# Subplot 3: Segundo aliasing
plt.figure(figsize=[10, 4])
data_alias2, t_alias2, datam_alias2, tm_alias2 = Acquisition_function(f_daq, f_sam)
plt.subplot(111)
plt.plot(t_alias2, data_alias2, label='Datos original', c='blue')
plt.stem(tm_alias2, datam_alias2, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
plt.xlabel('Tiempo (s)')
plt.legend(loc='upper right')
plt.title('Segundo aliasing')
plt.show()