
import streamlit as st

def show_metrics(energy, latency, firing_rate):
    col1, col2, col3 = st.columns(3)
    col1.metric("Energy", f"{energy:.2f}")
    col2.metric("Latency (steps)", latency)
    col3.metric("Avg Firing Rate", f"{firing_rate:.3f}")
