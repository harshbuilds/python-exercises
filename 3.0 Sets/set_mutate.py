# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set(map(int, input().split()))
ops = {
    'intersection_update': s.intersection_update,
    'update': s.update,
    'difference_update': s.difference_update,
    'symmetric_difference_update': s.symmetric_difference_update,
}
for _ in range(int(input())):
    cmd = input().split()
    data = map(int, input().split())
    ops[cmd[0]](data)

print(sum(s))
