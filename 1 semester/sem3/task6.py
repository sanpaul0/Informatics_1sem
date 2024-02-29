import numpy as np

tx = [3.39, 3.378, 3.367, 3.356, 3.344, 3.333, 3.322, 3.311, 3.300, 3.289, 3.279, 3.268, 3.257, 3.247]
ty = [8.63, 8.7, 8.77, 8.84, 8.9, 8.95, 8.99, 9.07, 9.12, 9.19, 9.24, 9.3, 9.36, 9.4]
#ty = [8.63, 8.7, 8.77, 8.84, 8.91, 8.96, 9.02, 9.07, 9.13, 9.18, 9.25, 9.3, 9.36, 9.4]
"""for i in range(len(tx)):
    tx[i] = tx[i]*0.001
    ty[i] = ty[i]*0.000001"""
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
