def wrapper(f):
    def fun(l):
        decorated =  []
        for phone in l:
            n = len(phone)
            start = n-10
            end = n-5
            decorated.append('+91 ' + ' '.join([str(phone)[start:end], str(phone)[end:]]))
        return f(decorated)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

