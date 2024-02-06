# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = set()
for _ in range(n):
    x = input()
    countries.add(x)
print(len(countries))
