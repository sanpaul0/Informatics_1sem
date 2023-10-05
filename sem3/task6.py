import numpy as np
tx = [0.505, 0.531, 0.549, 0.582, 0.637, 0.693, 0.779, 0.861]
ty = [0.109, 0.136, 0.153, 0.196, 0.254, 0.314, 0.396, 0.489]
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