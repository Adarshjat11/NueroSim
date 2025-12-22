# NueroSim
# Neuromorphic SNN Simulator and Analysis Platform

An interactive simulation and analysis framework for Spiking Neural Networks (SNNs),
designed to explore learning dynamics, neuron behavior, and efficiency in neuromorphic systems.
The platform enables users to configure different neuron models, apply biologically inspired
learning rules, visualize spiking activity, and analyze performance across training epochs.

---

## Overview

This project provides a configurable environment to:

- Simulate spiking neural networks with multiple neuron models
- Train networks using Spike-Timing-Dependent Plasticity (STDP)
- Visualize spike activity, synaptic weight evolution, and performance metrics
- Analyze the impact of different parameters and input conditions
- Import custom input data and export experimental results

The goal is to support experimentation, education, and early-stage research in
neuromorphic and brain-inspired computing.

---

## Key Features

### 🧠 Spiking Neuron Models
- Leaky Integrate-and-Fire (LIF)
- Integrate-and-Fire (IF)
- Izhikevich model
- Configurable parameters:
  - Threshold
  - Membrane decay
  - Reset potential
  - Refractory period

### 🔁 Learning Mechanism
- Spike-Timing-Dependent Plasticity (STDP)
- Adjustable learning rate
- Visualization of synaptic weight changes before and after learning

### 📥 Input Handling
- Upload input data in CSV or JSON format
- Support for time-series inputs (rows as timesteps, columns as neurons)
- Random input generation for quick experiments

### 📊 Visualization and Analysis
- Spike raster plots for neuron firing activity
- Synaptic weight heatmaps
- Performance dashboard tracking:
  - Accuracy
  - Energy efficiency
  - Latency reduction

### 🎛 Training and Experiment Control
- Multi-epoch training
- Early stopping using accuracy threshold
- Live performance updates during training
- Reset functionality to clear sessions

### 📤 Export and Reproducibility
- Export metrics as CSV
- Export full experiment results as JSON
- Download performance plots as images

### 🖥 Interactive Interface
- Built using Streamlit
- Clean layout with structured sections:
  - Performance dashboard
  - Neuron activity visualization
  - Synaptic learning analysis
  - Input data and configuration

---

## Motivation

Traditional artificial neural networks rely on continuous activations and dense computation,
often leading to high energy consumption. Spiking Neural Networks, inspired by biological neurons,
process information through discrete events over time, enabling sparse and energy-efficient computation.

This project aims to:
- Provide insight into spike-based computation
- Demonstrate biologically plausible learning through STDP
- Enable exploration of efficiency metrics beyond accuracy
- Serve as a practical tool for understanding neuromorphic principles

---

## Project Structure
NeuroSim/
├── neurosim/                       # Main Python package
│   ├── __init__.py
│   │
│   ├── simulator/
│   │   ├── __init__.py
│   │   ├── engine.py               # Simulation loop
│   │   ├── network.py              # Network topology
│   │   ├── neuron_models.py        # LIF, IF, Izhikevich
│   │   ├── synapse_models.py       # STDP learning
│   │   ├── metrics.py              # Energy, latency, accuracy
│   │   ├── input_utils.py          # CSV/JSON loader
│   │   └── export_utils.py         # CSV/JSON export
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── raster_plot.py          # Spike raster
│   │   ├── membrane_plot.py        # Vm vs time
│   │   ├── weight_plot.py          # Weight evolution
│   │   ├── performance.py          # Performance charts
│   │   └── dashboard.py            # Streamlit dashboard
│
├── app.py                          # Streamlit entry poin
├── .gitignore
├── README.md
└── setup.py                        # Package installation

---

## Algorithms Used

- **Leaky Integrate-and-Fire (LIF)** neuron model
- **Integrate-and-Fire (IF)** neuron model
- **Izhikevich** spiking neuron model
- **Spike-Timing-Dependent Plasticity (STDP)** learning rule

---

## How to Run

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
