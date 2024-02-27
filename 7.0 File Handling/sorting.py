import random
import time

def generate_file(filename, lines=5):
    data = ""
    for line in range(lines):
        data += "#"*random.randint(1,50) + "\n"
    with open("./{}".format(filename), mode='w') as f:
        f.write(data)

def slow_sort_file(filename):
    data = None
    with open("./{}".format(filename), mode='r') as f:
        data = f.readlines()
    for i, d in enumerate(data):
        idx = i
        while idx > 0 and len(data[idx]) < len(data[idx-1]):
            temp = (data[idx], data[idx-1])
            data[idx] = temp[1]
            data[idx-1] = temp[0]
            idx -= 1
            with open("./{}".format(filename), mode='w') as f:
                f.writelines(data)
            time.sleep(0.1)


if __name__ == "__main__":
    generate_file("test.txt", 25)
    slow_sort_file("test.txt")