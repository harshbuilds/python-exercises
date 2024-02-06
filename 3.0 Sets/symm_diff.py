# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
print(*sorted(a.symmetric_difference(b)), sep="\n")
