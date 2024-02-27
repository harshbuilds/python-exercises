import numpy as np
n = int(input().split()[0])
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print(np.max(np.min(np.array(arr), axis=1)))
