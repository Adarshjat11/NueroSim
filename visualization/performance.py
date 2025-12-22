
import matplotlib.pyplot as plt

def plot_performance(acc, energy, latency):
    epochs = list(range(1, len(acc) + 1))
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    axs[0].plot(epochs, acc, marker="o")
    axs[0].set_title("Accuracy over Epochs")
    axs[0].set_xlabel("Epoch")
    axs[0].set_ylabel("Accuracy")

    axs[1].plot(epochs, energy, marker="o")
    axs[1].set_title("Energy Consumption")
    axs[1].set_xlabel("Epoch")
    axs[1].set_ylabel("Energy (normalized)")

    axs[2].plot(epochs, latency, marker="o")
    axs[2].set_title("Latency Reduction")
    axs[2].set_xlabel("Epoch")
    axs[2].set_ylabel("Latency (ms)")

    fig.suptitle("Performance Dashboards")
    return fig
