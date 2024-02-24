import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16, 9))  # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(
    311)  # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(
    312)  # создали Axes ax2 в серии из 2 графиков, поставили на позицию [1,2] -- первый график во второй "строке" графиков
ax3 = fig.add_subplot(313)



values = np.random.normal(0, 20, 1000000)


ax1.hist(values, 50)
ax1.grid()

x = [i for i in range(50)]
y = [j ** 1.5 for j in x]
values = np.random.normal(0, 20, 100)


ax2.hist(values, 50)
ax2.grid()
values = np.random.normal(0, 20, 1000)


ax3.hist(values, 50)
ax3.grid()
values = np.random.normal(0, 20, 1000)
plt.show()