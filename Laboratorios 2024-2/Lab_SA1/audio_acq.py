'''
    Análisis de Señales
    2024-2
    Universidad Tecnológica de Pereira

    Práctica 1: Muestreo de señales de audio
'''

# Packages
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import io

# Frecuencias de muestreo: [1000, 2000, 3000] Hz
new_sample_rate = 650

# Dar click derecho en el archivo de audio y seleccionar "Copy Relative Path".
audio_path = "C:\\Users\\Admin\\Desktop\\Signals\\LabsSA_Local\\Lab1\\Lab1_local\\piano_music.wav"
audio_original = AudioSegment.from_wav(audio_path)

# Exportar el audio original a un buffer en memoria
buffer = io.BytesIO()
audio_original.export(buffer, format="wav")
buffer.seek(0)

# Leer el buffer con scipy.io.wavfile.read
sample_rate, audio_data = wavfile.read(buffer)
audio_data = audio_data[:, 1]

# Transformada de Fourier datos originales
x1 = np.fft.rfft(audio_data)
f1 = np.fft.rfftfreq(len(audio_data), d=1/sample_rate)

# Muestreo de la señal de audio
sample = audio_original.set_frame_rate(new_sample_rate)
audio_muestreado = sample.export("temp_sample.wav", format="wav")

sample_rate2, audio_data2 = wavfile.read(audio_muestreado)
audio_data2 = audio_data2[:, 1]

# Transformada de Fourier datos muestreados
x2 = np.fft.rfft(audio_data2)
f2 = np.fft.rfftfreq(len(audio_data2), d=1/sample_rate2)

# Gráficas
plt.figure(figsize=(10, 5))

plt.subplot(211)
plt.plot(f1, np.abs(x1)**2)
plt.title('Espectro de Frecuencias (Audio Original)')
plt.xlim(0, 3000)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

plt.subplot(212)
plt.plot(f2, np.abs(x2)**2)
plt.title('Espectro de Frecuencias (Audio Muestreado)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
