import numpy as np

ls = []
for i in range(int(input().split()[0])):
    row = list(map(int, input().split()))
    ls.append(row)
print(np.array(ls).transpose())
print(np.array(ls).flatten())
