import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('BTC_data.csv')
cost = list(df['close'])
date = list(df['time'])
ndate = map(lambda x: x[:-15], date)
ndate = list(ndate)

print(ndate)
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

ax1.plot(ndate,cost)
interval=[]
for i in range(len(ndate)):
    if i%150==0:
        interval.append(i)

print(interval)
ax1.set_xticks([interval[i] for i in range(len(interval))])
plt.show()


