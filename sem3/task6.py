import numpy as np
tx = [0, 0.0001, 0.0004, 0.0009, 0.0016, 0.0025, 0.0036, 0.0049, 0.0064]
ty = [0.00982, 0.01020, 0.01073, 0.01147, 0.01260, 0.01393, 0.01556, 0.01771, 0.02027]
x = np.array(tx)
y = np.array(ty)
x_mean = np.mean(x)
y_mean = np.mean(y)
numerator = (x - x_mean)*y
denominator = (x - x_mean)**2
a = np.sum(numerator)/np.sum(denominator)
b = y_mean - a*x_mean
Dyy = np.mean(y**2) - y_mean**2
Dxx = np.mean(x**2) - x_mean**2
sigma_a = np.sqrt(1/(len(tx)-2)*((Dyy/Dxx)-a**2))
sigma_b = sigma_a*np.sqrt(np.mean(x**2))
resa = f'a = {a}+-{sigma_a}'
resb= f'b = {b}+-{sigma_b}'
print(resa, resb, sep ='\n')