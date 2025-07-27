# Pendulum SNN

This repository provides code and conceptual materials for the **Pendulum Model of Spiking Neurons**, a biologically inspired alternative to traditional models like LIF and Izhikevich. The model is based on second-order dynamics of a damped driven pendulum and supports symbolic spike timing and phase-based STDP learning.

## Features

- Oscillatory and phase-aware neuron dynamics
- Spike-Timing Dependent Plasticity (STDP) learning
- Comparison with LIF and wheel models
- Simulations using Python and Brian2
- Notes for implementation on SpiNNaker hardware

## Getting Started

Install dependencies:

```bash
pip install -r requirements.txt

Run a single neuron simulation:
python single_neuron_sim.py

Reference
Bose, J. (2007). Engineering a Sequence Machine Using Spiking Neurons. University of Manchester, PhD Thesis.
