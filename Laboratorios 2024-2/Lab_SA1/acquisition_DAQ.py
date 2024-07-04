'''
    Análisis de Señales 
    2024-2
    Universidad Tecnológica de Pereira
    
    Práctica 1: Adquisición y muestreo de señales
'''

# Importar librerías
import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
import matplotlib.pyplot as plt
import numpy as np

# Parámetros de adquisición
f_daq = 5000  
f_sam = 10    
 
# Acquisition
def new_func(f_daq, f_sam):
    '''Función para adquirir y muestrear una señal.

    f_daq: Frecuencia de muestro de la DAQ  
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
    return data,time,datam,timem

data, time, datam, timem = new_func(f_daq, f_sam)

# Digitalización 
'''Realizar el código para la digitalización de la señal 
muestreada con n_bits de cuantización. Modificar apartir de 
la línea siguiente a la variable declarada 'n_bits = 2'
'''
n_bits = 2
####Código------------------------------------------------- 
digital_signal = np.zeros(len(datam))

####-------------------------------------------------------

# Gráficas
fig, axs = plt.subplots(2, 1, figsize=(12, 6))

# Subplot 1
axs[0].plot(time, data, label='Datos origial', c='blue')
axs[0].stem(timem, datam, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
axs[0].set_ylabel('Amplitud')
axs[0].set_title('Señal muestreada')
axs[0].legend(loc='upper right')
# Subplot 2
axs[1].plot(time, data, label='Datos origial', c='blue')
axs[1].step(time, digital_signal, where="post", c="r", label="Señal digital")
axs[1].set_ylabel('Amplitud')
axs[1].set_xlabel('Tiempo (s)')
axs[1].set_title('Señal digitalizada')
axs[1].legend(loc='upper right')

plt.show()