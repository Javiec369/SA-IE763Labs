import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
import matplotlib.pyplot as plt
import numpy as np

f_daq = 5000  
f_sam = 50    # Frecuencia de muestreo

# Adquisición de datos
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("myDAQ1/ai0")
    task.timing.cfg_samp_clk_timing(f_daq, sample_mode=AcquisitionType.FINITE, samps_per_chan=5000)
    data = task.read(READ_ALL_AVAILABLE)

data = np.array(data)
time = np.arange(0, len(data) / f_daq, 1 / f_daq)

factor = int(f_daq / f_sam)
datam = data[::factor]
timem = time[::factor]



# Graficar la señal original
plt.plot(time, data, label='Datos original')
plt.stem(timem, datam, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo (s)')
plt.title('Señal muestreada y digitalizada')
plt.legend()
plt.show()
