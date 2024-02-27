n = input()
arr = list(map(int, input().split()))
s = set(arr)
k = set()
for i in arr:
    if i in k:
        s.discard(i)
    else:
        k.add(i)
print(s.pop())
