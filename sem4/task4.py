import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris_data.csv')
SL = list(df['SepalLengthCm'])
SW = list(df['SepalWidthCm'])
PL = list(df['PetalLengthCm'])
PW = list(df['PetalWidthCm'])
fig1 = plt.figure(figsize = (2, 3))
ax1 = fig1.add_subplot(111)
ax1.scatter(SL, SW, marker='.', label ='SW(SL)' )
ax1.grid()

fig2 = plt.figure(figsize = (2, 3))
ax2 = fig2.add_subplot(111)
ax2.scatter(SL,PL, marker='.', label ='PL(SL)')
ax2.grid()


fig3 = plt.figure(figsize = (2, 3))
ax3 = fig3.add_subplot(111)
ax3.scatter(SW, PL, marker='.', label ='PL(SW)')
ax3.grid()

fig4 = plt.figure(figsize = (2, 3))
ax4 = fig4.add_subplot(111)
ax4.scatter(SL, PW, marker='.', label ='PW(SL)')
ax4.grid()

fig5 = plt.figure(figsize = (2, 3))
ax5 = fig5.add_subplot(111)
ax5.scatter(PL,PW, marker='.', label='PW(PL)')
ax5.grid()
#этот график больше всего похож на прямую

fig6 = plt.figure(figsize = (2, 3))
ax6 = fig6.add_subplot(111)
ax6.scatter(SW,PW, marker='.', label='PW(SW)')
ax6.grid()



z = np.polyfit(PL, PW, 1)
p = np.poly1d(z)
ax5.plot(PL,p(PL) , 'k')
plt.show()
print('МНК:', z)




