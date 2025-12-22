
import numpy as np
from simulator.network import SpikingNetwork

def run_simulation(steps, layers, model, params, lr, inputs=None):
    net = SpikingNetwork(layers, model, params, lr)
    spike_log, v_log, w_log = [], [], []

    for t in range(steps):
        if inputs is None:
            x = np.random.rand(layers[0])
        else:
            x = inputs[t]
        spikes, v, w = net.step(x)
        spike_log.append(spikes)
        v_log.append(v)
        w_log.append(w)

    return np.array(spike_log), np.array(v_log), np.array(w_log)
