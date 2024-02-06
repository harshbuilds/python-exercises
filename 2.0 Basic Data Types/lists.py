if __name__ == '__main__':
    N = int(input())
    arr = []
    ops = {
        'insert': arr.insert,
        'remove': arr.remove,
        'append': arr.append,
        'sort': arr.sort,
        'pop': arr.pop,
        'reverse': arr.reverse
    }
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'print':
            print(arr)
        else:
            if len(cmd) == 1:
                ops[cmd[0]]()
            elif len(cmd) == 2:
                ops[cmd[0]](int(cmd[1]))
            else:
                ops[cmd[0]](int(cmd[1]), int(cmd[2]))
    