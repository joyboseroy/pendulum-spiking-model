from brian2 import *
import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
duration = 500 * ms
dt = 0.1 * ms
defaultclock.dt = dt
steps = int(duration / dt)

# Input torque as angular acceleration
time_array = np.arange(steps) * float(dt / ms)
# Strong oscillatory input
input_current = (200 * np.sin(2 * np.pi * time_array / 50) + 250) / second**2
I_timed = TimedArray(input_current, dt=dt)

# Model equations
eqs = '''
dtheta/dt = omega : 1
domega/dt = -gamma * omega - omega0**2 * sin(theta) + I_timed(t) : 1/second
'''

# Parameters (tuned to spike)
gamma = 0.05 / ms
omega0 = 5.0 / ms

# Neuron group
G = NeuronGroup(1, model=eqs,
                threshold='theta > pi',
                reset='theta = 0; omega = 0*Hz',
                method='euler')

# Initial energy
G.theta = 0.1
G.omega = 5 * Hz

# Monitors
M = StateMonitor(G, ['theta', 'omega'], record=True)
spikemon = SpikeMonitor(G)

# Run
run(duration)

# Plot theta over time
plt.figure(figsize=(10, 4))
plt.plot(M.t/ms, M.theta[0], label='θ (angle)')
plt.axhline(np.pi, linestyle='--', color='red', label='Spike Threshold = π')
plt.scatter(spikemon.t/ms, [np.pi]*len(spikemon.t), color='orange', label='Spikes')
plt.xlabel('Time (ms)')
plt.ylabel('Theta (rad)')
plt.title('Pendulum Neuron: θ Dynamics and Spiking')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
