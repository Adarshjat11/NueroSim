
import matplotlib.pyplot as plt

def plot_weights(w):
    fig, ax = plt.subplots()
    ax.plot(w[:, 0])
    ax.set_title("STDP Weight Evolution (Synapse 0)")
    ax.set_xlabel("Time")
    ax.set_ylabel("Weight")
    return fig
