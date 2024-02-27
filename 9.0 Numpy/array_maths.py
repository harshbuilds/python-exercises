import numpy as np
n = input().split()[0]
a = []
for i in range(int(n)):
    a.append([int(i) for i in input().split()])
b = []
for i in range(int(n)):
    b.append([int(i) for i in input().split()])
a = np.array(a)
b = np.array(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
