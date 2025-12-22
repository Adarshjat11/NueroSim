
def compute_energy(spikes):
    return spikes.sum() * 0.1

def compute_latency(spikes):
    return len(spikes)

def compute_firing_rate(spikes):
    return spikes.mean()
