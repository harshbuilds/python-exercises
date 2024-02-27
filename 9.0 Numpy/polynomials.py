import numpy as np
p = list(map(float, input().split()))
x = int(input())
print(np.polyval(np.array(p), x))

# poly, roots, polyint, polyder, polyval, polyfit
# Also polyadd, polysub, polydiv, polymul
