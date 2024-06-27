'''
    Anális de Señales - 2024-2
    Práctica 1: Adquisición y muestreo de señales
'''

# Packages
import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
import matplotlib.pyplot as plt
import numpy as np

# Parameters
f_orig = 5000  
f_sam = 10    
n_bits = 2    



# Acquisition
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("myDAQ1/ai0")
    task.timing.cfg_samp_clk_timing(f_orig, sample_mode=AcquisitionType.FINITE, samps_per_chan=5000)
    data = task.read(READ_ALL_AVAILABLE)
data = np.array(data)
time = np.arange(0, len(data) / f_orig, 1 / f_orig)

factor = int(f_orig / f_sam)
datam = data[::factor]
timem = time[::factor]

# Digitalization
nc = (data.max() - data.min()) / (2 ** n_bits)
quantization_levels = [nc * i for i in range(2 ** n_bits + 1)]
xd = np.round((data - data.min()) / nc) * nc + data.min()

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(12, 6))

# Subplot 1
axs[0].plot(time, data, label='Datos origial', c='blue')
axs[0].stem(timem, datam, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
axs[0].set_ylabel('Amplitud')
axs[0].set_title('Señal muestreada')
axs[0].legend(loc='upper right')
# Subplot 2
axs[1].plot(time, data, label='Datos origial', c='blue')
axs[1].step(time, xd, where="post", c="r", label="Señal digital")
axs[1].set_ylabel('Amplitud')
axs[1].set_xlabel('Tiempo (s)')
axs[1].set_title('Señal digitalizada')
axs[1].legend(loc='upper right')

plt.show()
