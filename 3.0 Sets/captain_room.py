# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
arr = map(int, input().split())
s = set(arr)
k = set()
for i in arr:
    if i in k:
        s.remove(i)
    else:
        k.add(i)
print(s.pop())
