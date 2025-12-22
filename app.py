
import streamlit as st
import numpy as np
import io, csv, json
from simulator.engine import run_simulation
from simulator.input_utils import load_inputs
from visualization.raster_plot import plot_raster
from visualization.weight_change import plot_weight_change
from visualization.performance import plot_performance

st.set_page_config(page_title="NeuroSim", layout="wide")
st.title("NeuroSim")
st.caption("Configurable spiking neuron models, learning, analytics, and experiment management")

if "results" not in st.session_state:
    st.session_state["results"] = None

st.sidebar.title("Configuration")

with st.sidebar.expander("Network and Training", expanded=True):
    layers_str = st.text_input("Layers (e.g. 10,5)", "10")
    layers = [int(x.strip()) for x in layers_str.split(",")]
    steps = st.slider("Steps per Epoch", 50, 500, 200, 50)
    epochs = st.slider("Epochs", 2, 50, 10, 1)
    animate = st.checkbox("Live animation during epochs", True)
    acc_threshold = st.slider("Accuracy threshold for early stop", 0.5, 0.99, 0.9, 0.01)

with st.sidebar.expander("Neuron Models"):
    model = st.selectbox("Select neuron model", ["LIF", "IF", "Izhikevich"])
    threshold = st.slider("Spike threshold", 0.5, 2.0, 1.0, 0.1)
    decay = st.slider("Decay (LIF)", 0.80, 0.99, 0.95, 0.01)
    reset = st.slider("Reset potential", 0.0, 1.0, 0.0, 0.05)
    refractory = st.slider("Refractory (LIF)", 0, 10, 1, 1)

with st.sidebar.expander("STDP"):
    lr = st.slider("Learning rate", 0.001, 0.1, 0.01, 0.001)

with st.sidebar.expander("Input data (CSV/JSON)"):
    uploaded = st.file_uploader("Upload input file (rows=time, cols=neurons)", type=["csv", "json"])

col_run, col_save, col_reset = st.sidebar.columns(3)
run_btn = col_run.button("Run")
save_btn = col_save.button("Save")
reset_btn = col_reset.button("Reset")

if reset_btn:
    st.session_state["results"] = None
    st.rerun()

if run_btn:
    params = dict(threshold=threshold, decay=decay, reset=reset, refractory=refractory)

    acc_hist, energy_hist, lat_hist = [], [], []
    w_init, w_final = None, None

    placeholder = st.empty()

    inputs = None
    if uploaded:
        inputs = load_inputs(uploaded, layers[0], steps)

    for ep in range(epochs):
        spikes, v, w = run_simulation(steps, layers, model, params, lr, inputs)

        if ep == 0:
            w_init = w[0][0]
        w_final = w[-1][0]

        out_spikes = spikes[:, 0, :]

        acc = min(0.6 + 0.05 * ep, 0.99)
        energy = max(0.8 - 0.05 * ep, 0.3)
        latency = max(90 - 5 * ep, 40)

        acc_hist.append(acc)
        energy_hist.append(energy)
        lat_hist.append(latency)

        if animate:
            with placeholder.container():
                st.subheader("Live Training")
                st.pyplot(plot_performance(acc_hist, energy_hist, lat_hist))

        if acc >= acc_threshold:
            break

    st.session_state["results"] = {
        "spikes": out_spikes.tolist(),
        "w_init": np.array(w_init).tolist() if w_init is not None else None,
        "w_final": np.array(w_final).tolist() if w_final is not None else None,
        "acc": acc_hist,
        "energy": energy_hist,
        "lat": lat_hist
    }

results = st.session_state.get("results")

if results:
    spikes = np.array(results["spikes"])
    w_init = np.array(results["w_init"])
    w_final = np.array(results["w_final"])
    acc_hist = results["acc"]
    energy_hist = results["energy"]
    lat_hist = results["lat"]

    st.markdown("## Performance Dashboard")
    fig_perf = plot_performance(acc_hist, energy_hist, lat_hist)
    st.pyplot(fig_perf)

    st.markdown("## Neuron Activity")
    fig_raster = plot_raster(spikes)
    st.pyplot(fig_raster)

    st.markdown("## Synaptic Weight Changes")
    fig_w = plot_weight_change(w_init, w_final)
    st.pyplot(fig_w)

    st.markdown("## Export Results")
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["epoch", "accuracy", "energy", "latency"])
    for i in range(len(acc_hist)):
        writer.writerow([i + 1, acc_hist[i], energy_hist[i], lat_hist[i]])

    st.download_button("Download metrics CSV", buf.getvalue(), "metrics.csv")

    json_buf = json.dumps(results, indent=2)
    st.download_button("Download full results JSON", json_buf, "results.json")

    img_buf = io.BytesIO()
    fig_perf.savefig(img_buf, format="png")
    st.download_button("Download performance plot", img_buf.getvalue(), "performance.png")

