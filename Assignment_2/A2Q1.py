#Q1 pzmap
import control
import matplotlib.pyplot as plt

#%%
#part a
G1 = control.tf([1,2,1],[1,5,6])
map =  control.pzmap(G1)
plt.legend(['G1'])
plt.show()

#%%
#part b
G2 = control.tf([1,0.5],[1,1,2])
map =  control.pzmap(G2)
plt.legend(['G2'])
plt.show()
#%%
#part c
G3 = control.tf([1,8,19,12],[1,7,10])
map =  control.pzmap(G3)
#legend
plt.legend(['G3'])

plt.show()

