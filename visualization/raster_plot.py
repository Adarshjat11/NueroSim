
import matplotlib.pyplot as plt
import numpy as np

def plot_raster(spikes):
    fig, ax = plt.subplots()
    T, N = spikes.shape
    for n in range(N):
        ts = np.where(spikes[:, n] > 0)[0]
        ax.vlines(ts, n + 0.5, n + 1.5)
    ax.set_ylim(0.5, N + 0.5)
    ax.set_xlabel("Time")
    ax.set_ylabel("Neuron Index")
    ax.set_title("Basic Spike Raster Visualization")
    return fig
