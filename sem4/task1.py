import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(111)
U = np.array([0, 0.0001, 0.0004, 0.0009, 0.0016, 0.0025, 0.0036, 0.0049, 0.0064])
V = np.array([0.00982, 0.01020, 0.01073, 0.01147, 0.01260, 0.01393, 0.01556, 0.01771, 0.02027])
ax1.scatter(U, V, marker='.', label='V(U)')
z = np.polyfit(U, V, 1)
p = np.poly1d(z)
ax1.errorbar(U, V, yerr=0.00002, xerr=0.0001, color='k', linestyle='None')
ax1.plot(U, p(U), 'k')
print(z)
plt.title('График I(h^2)', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('h^2, см^2')
plt.ylabel('I, г*м^2')
ax1.grid()
plt.show()
