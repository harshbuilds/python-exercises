import numpy as np
n = 2
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
x = np.array(arr[0])
y = np.array(arr[1])
print(np.inner(x, y))
print(np.outer(x, y))
