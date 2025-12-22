
from simulator.neuron_models import LIFNeuron, IFNeuron, IzhikevichNeuron
from simulator.synapse_models import STDP

class SpikingNetwork:
    def __init__(self, layers, model, params, lr):
        self.layers = []
        self.weights = []
        self.stdp = STDP(lr=lr)
        self.model = model
        self.params = params

        for n in layers:
            if model == "LIF":
                layer = [LIFNeuron(**params) for _ in range(n)]
            elif model == "IF":
                layer = [IFNeuron(**params) for _ in range(n)]
            elif model == "Izhikevich":
                layer = [IzhikevichNeuron() for _ in range(n)]
            else:
                layer = [LIFNeuron(**params) for _ in range(n)]
            self.layers.append(layer)
            self.weights.append([0.5] * n)

    def step(self, inputs):
        layer_input = inputs
        all_spikes, all_v, all_w = [], [], []

        for li, layer in enumerate(self.layers):
            spikes, voltages = [], []
            for i, neuron in enumerate(layer):
                spike, v = neuron.step(layer_input[i] * self.weights[li][i])
                self.weights[li][i] = self.stdp.update(self.weights[li][i], layer_input[i] > 0.5, spike)
                spikes.append(spike)
                voltages.append(v)
            layer_input = spikes
            all_spikes.append(spikes)
            all_v.append(voltages)
            all_w.append(list(self.weights[li]))
        return all_spikes, all_v, all_w
