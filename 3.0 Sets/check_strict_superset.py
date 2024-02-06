# Enter your code here. Read input from STDIN. Print output to STDOUT
sup = set(input().split())
ans = True
for _ in range(int(input())):
    ans &= set(input().split()).issubset(sup)
print(ans)


