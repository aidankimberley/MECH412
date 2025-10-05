#Q3 pzmap

import control
import matplotlib.pyplot as plt

G1 = control.tf([1,1],[1,1,2])
G2 = control.tf([8,42,140,138],[1,6,28,74,51])
G3 = control.tf([1],[1,-2,3,-2])
G4 = control.tf([1,2],[1,0.5,0.5,0.25,0])

#%%
control.pzmap(G1)
plt.show()
tout, yout = control.step_response(G1)
plt.plot(tout, yout)
plt.title('Step Response of G1')
plt.show()
tout, yout = control.impulse_response(G2)
plt.plot(tout, yout)
plt.title('Impulse Response of G1')
plt.show()
#%%
control.pzmap(G2)
plt.show()
tout, yout = control.step_response(G2)
plt.plot(tout, yout)
plt.title('Step Response of G2')
#title: Step Response
plt.title('Step Response of G2')

plt.show()
tout, yout = control.impulse_response(G2)
plt.plot(tout, yout)
plt.show()
#%%
control.pzmap(G3)
plt.show()
tout, yout = control.step_response(G3)
plt.plot(tout, yout)
plt.title('Step Response of G3')
plt.show()
tout, yout = control.impulse_response(G3)
plt.plot(tout, yout)
plt.title('Impulse Response of G3')
plt.show()
#%%
control.pzmap(G4)
plt.show()
tout, yout = control.step_response(G4)
plt.plot(tout, yout)
plt.title('Step Response of G4')
plt.show()
tout, yout = control.impulse_response(G4)
plt.plot(tout, yout)
plt.title('Impulse Response of G4')
plt.show()
#%%