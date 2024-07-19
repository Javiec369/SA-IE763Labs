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
def acquisition_function(f_daq, f_sam):
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

def create_plots(title, f_daq, f_sam):
    '''
    Función para crear gráficas de las señales originales y muestreadas.
    title: Título de la gráfica
    f_daq: Frecuencia de muestreo DAQ
    f_sam: Frecuencia de muestreo de la señal

    y: Señal original
    t: Tiempo de la señal original
    y_muestras: Señal muestreada
    t_muestras: Tiempo de la señal muestreada
    '''
    y, t, y_muestras, t_muestras = acquisition_function(f_daq, f_sam)
    plt.figure(figsize=[10, 5])
    plt.plot(t, y, label='Datos original',c='blue')
    plt.stem(t_muestras, y_muestras, linefmt='r-',markerfmt='ro',basefmt='r-',label='Señal muestreada')
    plt.xlabel('Tiempo (s)')
    plt.legend(loc='upper right')
    plt.title(title)
    plt.show()

create_plots('Señal original y muestreada', f_daq, f_sam)
create_plots('Primer aliasing de la señal', f_daq, f_sam)
create_plots('Segundo aliasing de la señal', f_daq, f_sam)