n, m = input().split()
arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ans = 0
for i in arr:
    if i in a:
        ans += 1
    if i in b:
        ans -= 1
        
print (ans)
