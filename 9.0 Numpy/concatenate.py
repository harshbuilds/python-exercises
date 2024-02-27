import numpy as np

n, m, p = [int(i) for i in input().split()]
narr, marr = [], []
for i in range(n):
    narr.append([int(i) for i in input().split()])
    
for i in range(m):
    marr.append([int(i) for i in input().split()])

print(np.concatenate((narr, marr)))
