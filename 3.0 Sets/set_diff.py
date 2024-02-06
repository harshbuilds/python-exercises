# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set(input().split())
n = input()
k = set(input().split())
print(len(s-k))
