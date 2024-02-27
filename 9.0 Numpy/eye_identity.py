import numpy as np
a = input().split()
np.set_printoptions(legacy='1.13')
print(np.eye(int(a[0]), int(a[1])))
