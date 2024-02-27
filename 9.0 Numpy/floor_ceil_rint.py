import numpy as np

ls = np.array(list(map(float, input().split())))
np.set_printoptions(legacy='1.13')
print(np.floor(ls))
print(np.ceil(ls))
print(np.rint(ls))
