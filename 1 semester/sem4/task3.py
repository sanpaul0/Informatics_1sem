import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('iris_data.csv')
setosa, versicolor, virginica = 0, 0, 0
short, medium, long = 0, 0, 0
for i in range(len(list(df['Species']))):
    if list(df['Species'])[i] == 'Iris-setosa':
        setosa+=1
    elif list(df['Species'])[i] == 'Iris-versicolor':
        versicolor+=1
    else:
        virginica+=1
for i in range(len(list(df['PetalLengthCm']))):
    if list(df['PetalLengthCm'])[i]<1.2:
        short+=1
    if 1.2<= list(df['PetalLengthCm'])[i] <= 1.5:
        medium+=1
    if list(df['PetalLengthCm'])[i]>= 1.2:
        long+=1
fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(211) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(212)
ax1.pie([setosa/(len(list(df['Species']))), versicolor/(len(list(df['Species']))), virginica/(len(list(df['Species'])))], labels = ['Iris setosa','Iris versicolor','Iris virginica'])
ax1.set_title('Species')
ax2.pie([short/(len(list(df['Species']))), medium/(len(list(df['Species']))), long/(len(list(df['Species'])))], labels = ['Short', 'Medium','Long'])
ax2.set_title('Pental length')

plt.show()
