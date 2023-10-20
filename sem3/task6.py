import numpy as np
tx = [4.65, 9.03, 14.07, 7.25, 9.05, 12.95, 17.57, 25.1]
ty = [0.48, 0.878, 1.311, 0.724, 0.911, 1.199, 1.652, 2.309]
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