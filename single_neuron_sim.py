import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
T = 500
dt = 0.1
steps = int(T / dt)
time = np.linspace(0, T, steps)

# Pendulum neuron parameters
gamma = 0.05
omega0 = 1.0
threshold = np.pi
theta = np.zeros(steps)
dtheta = np.zeros(steps)
spikes = np.zeros(steps)

def input_current(t):
    return 1.5 * np.sin(0.01 * t) + 1.2

# Euler simulation
for i in range(1, steps):
    I = input_current(time[i])
    ddtheta = -gamma * dtheta[i-1] - omega0**2 * np.sin(theta[i-1]) + I
    dtheta[i] = dtheta[i-1] + ddtheta * dt
    theta[i] = theta[i-1] + dtheta[i] * dt
    if theta[i] >= threshold:
        spikes[i] = 1
        theta[i] = 0
        dtheta[i] = 0

# Plot results
plt.plot(time, theta, label='Phase θ')
plt.axhline(threshold, color='red', linestyle='--', label='Threshold π')
plt.scatter(time[spikes == 1], [threshold]*int(np.sum(spikes)), color='orange', label='Spikes')
plt.title('Pendulum Neuron Simulation')
plt.xlabel('Time (ms)')
plt.ylabel('Phase θ')
plt.legend()
plt.grid(True)
plt.show()
