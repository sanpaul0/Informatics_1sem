import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)
U = np.array([0.505, 0.531, 0.549, 0.582, 0.637, 0.693, 0.779, 0.861])
V = np.array([0.109, 0.136, 0.153, 0.196, 0.254, 0.314, 0.396, 0.489])
ax1.scatter(U,V, marker='.', label='V(U)')
z = np.polyfit(U, V, 1)
p = np.poly1d(z)
ax1.plot(U,p(U) , 'k')
print(z)
plt.title('График для определения ускорения свободного падения.', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('u, м*с^2')
plt.ylabel('v, м^2')
ax1.grid()
plt.show()



