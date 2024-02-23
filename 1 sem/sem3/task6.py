import numpy as np

tx = [3.40, 3.30, 3.19, 3.09, 3.00]
ty = [-1.16, -1.13, -1.05, -0.94, -0.87]
for i in range(len(tx)):
    tx[i] = tx[i]*0.001
    ty[i] = ty[i]*0.000001
x = np.array(tx)
y = np.array(ty)
x_mean = np.mean(x)
y_mean = np.mean(y)
numerator = (x - x_mean) * y
denominator = (x - x_mean) ** 2
a = np.sum(numerator) / np.sum(denominator)
b = y_mean - a * x_mean
Dyy = np.mean(y ** 2) - y_mean ** 2
Dxx = np.mean(x ** 2) - x_mean ** 2
sigma_a = np.sqrt(1 / (len(tx) - 2) * ((Dyy / Dxx) - a ** 2))
sigma_b = sigma_a * np.sqrt(np.mean(x ** 2))
resa = f'a = {a}+-{sigma_a}'
resb = f'b = {b}+-{sigma_b}'
print(resa, resb, sep='\n')
