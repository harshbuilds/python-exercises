import numpy as np

a = [int(i) for i in input().split()]
print(np.zeros(tuple(a), dtype=np.int))
print(np.ones(tuple(a), dtype=np.int))
