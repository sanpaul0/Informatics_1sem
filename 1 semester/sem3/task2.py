import numpy as np
N = int(input())
max_divider = N
sqr = np.sqrt(N)
dividers = []
i = 2
while i < (int(sqr)+1):
    if N % i == 0:
        N = N // i
        dividers.append(i)
        i -= 1
    i += 1
for i in range(len(dividers)):
    max_divider /= dividers[i]
dividers.append(int(max_divider))
print(dividers)

