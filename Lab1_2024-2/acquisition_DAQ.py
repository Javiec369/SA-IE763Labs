import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
import matplotlib.pyplot as plt
import numpy as np


f_orig = 5000  
f_sam = 30     
n_bits = 2    

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("myDAQ1/ai0")
    task.timing.cfg_samp_clk_timing(f_orig, sample_mode=AcquisitionType.FINITE, samps_per_chan=5000)
    data = task.read(READ_ALL_AVAILABLE)

data = np.array(data)


time = np.arange(0, len(data) / f_orig, 1 / f_orig)


factor = int(f_orig / f_sam)
datam = data[::factor]
timem = time[::factor]
nc = (data.max() - data.min()) / (2 ** n_bits)
quantization_levels = [nc * i for i in range(2 ** n_bits + 1)]
xd = np.round((data - data.min()) / nc) * nc + data.min()


fig, ax = plt.subplots()
ax.plot(time, data, label='Datos origial')
ax.stem(timem, datam, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal muestreada')
ax.step(time, xd, where="post", c="g", label="Señal digital")

secax = ax.secondary_yaxis('right')
secax.set_yticks(quantization_levels)
secax.set_yticklabels([format(int(i/nc), f'0{n_bits}b') for i in quantization_levels], fontsize=10)

ax.set_ylabel('Amplitud')
ax.set_xlabel('Tiempo (s)')
ax.set_title('Señal muestreada y digitalizada')
ax.legend()
plt.show()