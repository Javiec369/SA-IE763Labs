import numpy as np
import matplotlib.pyplot as plt

# Plotting signals function
def signal_plots(U_12, U_23, U_31, I_1, I_2, I_3, f_s, Xlim):
    '''
    Function to generate four subplots of voltage and current signals,
    visualizing both in the time domain and sample domain.

    Parameters:
    - U_12, U_23, U_31: Voltage signal arrays (Line-to-line voltages)
    - I_1, I_2, I_3: Current signal arrays (Line currents)
    - f_s: Sampling frequency of device PQ3198
    - Xlim: Limit for the number of samples or time to display on the X-axis

    The function generates two rows of plots:
    - Top row: Voltage signals in both time domain and sample domain
    - Bottom row: Current signals in both time domain and sample domain

    Time domain plots have time (seconds) on the X-axis, while sample domain
    plots display data based on sample indices.
    '''
    # Number of samples
    N = len(U_12)
    # Create time vector based on the sampling frequency
    t = np.linspace(0, N / f_s, N)

    # Create figure and subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 6))

    '''Voltage signals in the time domain (subplot at position 0,0)'''
    axs[0, 0].plot(t, U_12, label='U12')
    axs[0, 0].plot(t, U_23, label='U23')
    axs[0, 0].plot(t, U_31, label='U31')
    axs[0, 0].set_xlabel('Time [s]')
    axs[0, 0].set_ylabel('Voltage [V]')
    axs[0, 0].set_title('Voltage signals (Time domain)')
    axs[0, 0].legend(loc='upper right')
    axs[0, 0].grid(True)
    axs[0, 0].set_xlim(0, Xlim / f_s)

    '''Voltage signals in the sample domain (subplot at position 0,1)'''
    axs[0, 1].plot(U_12, label='U12')
    axs[0, 1].plot(U_23, label='U23')
    axs[0, 1].plot(U_31, label='U31')
    axs[0, 1].set_xlabel('Samples')
    axs[0, 1].set_ylabel('Voltage [V]')
    axs[0, 1].set_title('Voltage signals (Samples domain)')
    axs[0, 1].legend(loc='upper right')
    axs[0, 1].grid(True)
    axs[0, 1].set_xlim(0, Xlim)

    '''Current signals in the time domain (subplot at position 1,0)'''
    axs[1, 0].plot(t, I_1, label='I1')
    axs[1, 0].plot(t, I_2, label='I2')
    axs[1, 0].plot(t, I_3, label='I3')
    axs[1, 0].set_xlabel('Time [s]')
    axs[1, 0].set_ylabel('Current [A]')
    axs[1, 0].set_title('Current signals (Time domain)')
    axs[1, 0].legend(loc='upper right')
    axs[1, 0].grid(True)
    axs[1, 0].set_xlim(0, Xlim / f_s)

    axs[1, 1].plot(I_1, label='I1')
    axs[1, 1].plot(I_2, label='I2')
    axs[1, 1].plot(I_3, label='I3')
    axs[1, 1].set_xlabel('Samples')
    axs[1, 1].set_ylabel('Current [A]')
    axs[1, 1].set_title('Current signals (Samples domain)')
    axs[1, 1].legend(loc='upper right')
    axs[1, 1].grid(True)
    axs[1, 1].set_xlim(0, Xlim)

    '''Adjust layout for better visualization'''
    plt.tight_layout()
    plt.show()