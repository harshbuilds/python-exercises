if __name__ == '__main__':
    first = [200]
    second = [200]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < first[0]:
            second = first
            first = [score, name]
        elif score == first[0]:
            first.append(name)
        elif score < second[0]:
            second = [score, name]
        elif score == second[0]:
            second.append(name)
    print(*sorted(second[1:]), sep="\n")
    