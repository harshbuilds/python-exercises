if __name__ == '__main__':
    n = int(input())
    print(sorted(set(input().split()), key=int)[-2])
