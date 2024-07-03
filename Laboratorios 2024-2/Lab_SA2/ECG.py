from pyfirmata2 import Arduino
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
from scipy import signal


PORT = Arduino.AUTODETECT
BUFFER_SIZE = 5000
SAMPLING_RATE = 1000
CSV_FILE_PATH = 'recorded_data.csv'



class RealtimePlotWindow:

    def __init__(self, buffer_size, sampling_rate):
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, gridspec_kw={'hspace': 0})
        self.plotbuffer = np.zeros(buffer_size)
        self.line, = self.ax1.plot(self.plotbuffer)
        self.ringbuffer = []
        self.fft_line, = self.ax2.plot([], [])
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100)
        self.buffer_size = buffer_size
        self.sampling_rate = sampling_rate

        # Add grid and labels
        self.ax1.grid(True)
        self.ax1.set_ylabel('Amplitude')
        self.ax1.margins(x=0)
        self.ax2.grid(True)
        self.ax2.set_xlabel('Frequency (Hz)')
        self.ax2.set_ylabel('Magnitude')

        # Connect closing event to save data
        self.fig.canvas.mpl_connect('close_event', self.save_data)

        # Create an empty CSV file
        with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
            pass

    def update(self, data):
        self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
        self.plotbuffer = self.plotbuffer[-self.buffer_size:]
        self.save_data()  # Save data each time the buffer is updated
        self.ringbuffer = []
        self.line.set_ydata(self.plotbuffer)
        self.update_fft_plot()
        self.update_y_limits()
        return self.line, self.fft_line

    def addData(self, v):
        self.ringbuffer.append(v)

    def update_fft_plot(self):
        N = len(self.plotbuffer)
        fft_data = np.fft.rfft(self.plotbuffer, norm="forward")
        fft_data[0] = 0.0
        freq = np.fft.rfftfreq(N, d=1.0/self.sampling_rate)
        mag = np.abs(fft_data)
        self.fft_line.set_xdata(freq)
        self.fft_line.set_ydata(mag)
        self.ax2.set_xlim(0, 500)  # Adjust x-axis limit to show only positive frequencies

    def update_y_limits(self):
        eps = 1e-6
        min_y1 = np.min(self.plotbuffer)
        max_y1 = np.max(self.plotbuffer) + eps
        min_y2 = 0
        max_y2 = np.max(np.abs(self.fft_line.get_ydata())) * 1.1 + eps
        self.ax1.set_ylim(min_y1, max_y1)
        self.ax2.set_ylim(min_y2, max_y2)

    def save_data(self):
        with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(map(list, zip(*[self.plotbuffer])))

def main():
    realtimePlotWindow = RealtimePlotWindow(BUFFER_SIZE, SAMPLING_RATE)

    def callBack(data):
        realtimePlotWindow.addData(data)

    board = Arduino(PORT)
    board.samplingOn(1000 / SAMPLING_RATE)
    analog_pin = 0  # Modify this according to the analog pin connected to the sensor
    board.analog[analog_pin].register_callback(callBack)
    board.analog[analog_pin].enable_reporting()

    plt.show()

    board.exit()
    print("finished")

if __name__ == "__main__":
    main()