
import matplotlib.pyplot as plt
import numpy as np

def _ensure_2d(w):
    w = np.array(w)
    if w.ndim == 1:
        return w.reshape(1, -1)
    return w

def plot_weight_change(w_init, w_final):
    w_init = _ensure_2d(w_init)
    w_final = _ensure_2d(w_final)

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    im0 = axs[0].imshow(w_init, aspect="auto")
    axs[0].set_title("Initial Weights")
    fig.colorbar(im0, ax=axs[0], fraction=0.046)

    im1 = axs[1].imshow(w_final, aspect="auto")
    axs[1].set_title("Final Weights")
    fig.colorbar(im1, ax=axs[1], fraction=0.046)

    fig.suptitle("Weight Change Visualization")
    fig.tight_layout()
    return fig
