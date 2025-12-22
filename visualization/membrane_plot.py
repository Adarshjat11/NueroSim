
import matplotlib.pyplot as plt

def plot_membrane(v):
    fig, ax = plt.subplots()
    ax.plot(v[:, 0])
    ax.set_title("Membrane Potential (Neuron 0)")
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage")
    return fig
