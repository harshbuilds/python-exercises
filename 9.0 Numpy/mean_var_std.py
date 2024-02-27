import numpy as np
n = int(input().split()[0])
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
x = np.array(arr)

# np.set_printoptions(legacy='1.13')
print(np.mean(x, axis=1))
print(np.var(x, axis=0))
print(round(np.std(x), 11))
