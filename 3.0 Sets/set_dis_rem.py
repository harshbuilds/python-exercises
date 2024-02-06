n = int(input())
s = set(map(int, input().split()))
ops = {
    'pop': s.pop,
    'remove': s.remove,
    'discard': s.discard,
}
for _ in range(int(input())):
    cmd = input().split()
    if len(cmd) == 1:
        ops[cmd[0]]()
    else:
        ops[cmd[0]](int(cmd[1]))
    # print(s)

print(sum(s))