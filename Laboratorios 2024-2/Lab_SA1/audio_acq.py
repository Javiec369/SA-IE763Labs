'''
    Anális de Señales - 2024-2
    Práctica 1: Muestreo de señales de audio
'''

# Packages
from pydub import AudioSegment
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, rfft, rfftfreq
from scipy.io import wavfile

# Frecuencias de muestreo: [1000, 2000, 3000] Hz
new_sample_rate = 2000

# Se requiere el path del archivo de audio
# Dar click derecho en el archivo de audio y seleccionar "Copy Relative Path".
audio_path = r"Lab1_2024-2\\piano_music.mp3"

audio = AudioSegment.from_mp3(audio_path)
d = audio.export("audio.wav", format="wav")

def upload_and_resample_audio(new_sample_rate):
    resampled_audio = audio.set_frame_rate(new_sample_rate)

    #Asignar un nombre al archivo temporal que crearemos
    # ruta: nombre_carpeta\\temp_audio.wav
    temp_file = r"ruta"
    resampled_audio.export(temp_file, format="wav")


upload_and_resample_audio(new_sample_rate)

#Aplicar la fft en ambas señales de audio el original y el muestreada

sample_rate, audio_data = wavfile.read(d)
audio_data = audio_data[:, 1]

x = np.fft.rfft(audio_data)
frecuencia = np.fft.rfftfreq(len(audio_data), d=1/sample_rate)

audio2 = AudioSegment.from_wav(r"ruta")
s=audio2.export("temp2.wav", format="wav")

sample_rate2, audio_data2 = wavfile.read(s)
audio_data2 = audio_data2[:, 1]

x1 = np.fft.rfft(audio_data2)
frecuencia1 = np.fft.rfftfreq(len(audio_data2), d=1/sample_rate2)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(frecuencia, np.abs(x)**2)
plt.title('Espectro de Frecuencias (Audio Original)')
plt.xlim(0, new_sample_rate)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

plt.subplot(2, 1, 2)
plt.plot(frecuencia1, np.abs(x1)**2)
plt.title('Espectro de Frecuencias (Audio Muestreado)')
plt.xlim(0, new_sample_rate/2)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()