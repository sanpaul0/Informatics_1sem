import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(111)
V1 = np.array([12.2, 13, 12.8, 12.7, 12.6, 12.5, 12.4,
               12.3])  # ([117.72, 147.15, 176.58, 196.20, 215.82, 235.44, 255.06, 274.68])
V2 = np.array(
    [2.98472254911633, 2.98103377989378, 2.93641343573331, 2.89957111049592, 2.87726470684672, 2.86837450007153,
     2.80636517588166, 2.79691181686325])  # ([176.58, 196.2, 215.82, 235.44, 255.06, 274.68, 294.30,313.92])
V3 = np.array(
    [12.3898083631712, 11.3846517280886, 11.2388286620679, 11.3846966654197, 11.0490553036277, 11.138110789148,
     11.1092931031319, 11.0412399550885])  # ([451.26, 470.88, 490.5, 510.12, 529.74, 559.17, 588.60, 618.03])
# V4 = np.array([170.69])
# V5 = np.array([68.67])
# V6 = np.array([101.24])"""
U1 = np.array([939, 1017, 1122, 1187, 1249, 1314, 1375, 1430])  # ([131, 139.6, 143.4, 145.3, 150.3, 153.8, 158, 162.4])
U2 = np.array(
    [1512, 1676, 1771, 1862, 1945, 2022, 2116, 2189])  # ([137, 144.5, 152.7, 160.5, 167.7, 174.3, 182.4, 188.7])
U3 = np.array(
    [1112, 1185, 1217, 1234, 1276, 1306, 1341, 1379])  # ([131, 139.6, 143.4, 145.3, 150.3, 153.8, 158, 162.4])"""
# U4 = np.array([11.5])
# U5 = np.array([6])
# U6 = np.array([11])
ax1.scatter(U1, V1, marker='.', label='Труба 1')
ax1.scatter(U2, V2, marker='^', label='Труба 2')
ax1.scatter(U3, V3, marker='s', label='Труба 3')
"""
ax1.plot(U4, V4,'k.', marker='.')
ax1.plot(U5, V5, 'r^', marker='^')
ax1.plot(U6, V6, 'bs',  marker='s')"""
x = np.polyfit(U1, V1, 1)
# y = np.polyfit(U2, V2, 1)
# z = np.polyfit(U3, V3, 1)
p = np.poly1d(x)
# m = np.poly1d(y)
# n = np.poly1d(z)
ax1.errorbar(U1, V1, yerr=0.000000001, xerr=0.00019, color='k', linestyle='None')
ax1.errorbar(U2, V2, yerr=0.0001, xerr=0.00019, color='r', linestyle='None')
ax1.errorbar(U3, V3, yerr=0.0001, xerr=0.00019, color='b', linestyle='None')
"""ax1.plot(U1, p(U1), 'k')
ax1.plot(U2, m(U2), 'r')
ax1.plot(U3, n(U3), 'b')"""
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.title('', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
ax1.grid()
plt.legend()
plt.show()
