import numpy as np
tx = [66.5, 108.5, 137.7, 212.3, 259.5, 322.8, 403.8]
ty = [34.1, 58.1, 70.7, 109.8, 132.4, 164.6, 206.1]
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