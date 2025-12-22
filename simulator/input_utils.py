
import json, csv
import numpy as np

def load_inputs(file, neurons, steps):
    name = file.name.lower()
    if name.endswith(".json"):
        data = json.load(file)
        return np.array(data)[:steps, :neurons]
    elif name.endswith(".csv"):
        reader = csv.reader(file.read().decode().splitlines())
        rows = [[float(x) for x in r] for r in reader]
        return np.array(rows)[:steps, :neurons]
    else:
        raise ValueError("Unsupported format")
