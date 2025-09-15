
#%% 
# Imports
import control
import matplotlib as plt
from matplotlib import pyplot as plt
import numpy as np

#%% 
# Parameters
t_start = 0 
t_end = 10 
dt = 1e-2
t = np.arange(t_start, t_end, dt)
# Example transfer function definitions:

# First-order transfer function: G(s) = K/(τs + 1)
# where K is the gain and τ is the time constant
K = 12  # gain
tau = 4  # time constant
G = control.TransferFunction([K], [tau, 1])

print("Transfer function G(s):")
print(G)

#%%
# Impulse response
t_imp, y_imp = control.impulse_response(G, t)

fig, ax = plt.subplots()
ax.plot(t_imp, y_imp)
plt.xlabel('Time (s)')
plt.ylabel('Impulse response')
fig.tight_layout()
plt.show()

#%%
# Step response new function
G = control.tf([3], [1,2,4])
print("Transfer function G(s):")
print(G)
t_step, y_step = control.step_response(G, t)

fig, ax = plt.subplots()
ax.plot(t_step, y_step)
plt.xlabel('Time (s)')
plt.ylabel('Step response')
fig.tight_layout()
plt.show()