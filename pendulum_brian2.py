from brian2 import *

# Simulation parameters
duration = 500*ms
defaultclock.dt = 0.1*ms

# Pendulum model equations
eqs = '''
dtheta/dt = omega : 1
domega/dt = -gamma * omega - omega0**2 * sin(theta) + I : 1
I : 1
'''

# Parameters
gamma = 0.05
omega0 = 1.0

# Create neuron group
G = NeuronGroup(1, model=eqs, threshold='theta > pi', reset='theta = 0; omega = 0', method='euler')
G.theta = 0
G.omega = 0
G.I = 1.5 * np.sin(0.01 * np.arange(int(duration/defaultclock.dt))) + 1.2

# Monitors
M = StateMonitor(G, ['theta', 'omega'], record=True)
spikemon = SpikeMonitor(G)

# Run simulation
run(duration)

# Plot results
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
plt.plot(M.t/ms, M.theta[0], label='Phase θ (Brian2)')
plt.axhline(np.pi, color='red', linestyle='--', label='Threshold π')
plt.scatter(spikemon.t/ms, [np.pi]*len(spikemon.t), color='orange', label='Spikes')
plt.xlabel('Time (ms)')
plt.ylabel('θ (radians)')
plt.title('Pendulum Neuron in Brian2')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
