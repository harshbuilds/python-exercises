import numpy as np
n = int(input().split()[0])
arr, brr = [], []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    brr.append(list(map(int, input().split())))
x = np.array(arr)
y = np.array(brr)

print(np.dot(arr, brr))