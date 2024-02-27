import numpy as np
n = int(input().split()[0])
arr = []
for i in range(n):
    arr.append(list(map(float, input().split())))
x = np.array(arr)
print(round(np.linalg.det(x), 2))

# http://docs.scipy.org/doc/numpy/reference/routines.linalg.html

