# Use pypy3 as interpreter
import re

for _ in range(int(input())):
    try:
        a = re.compile(input())
        print(True)
    except Exception as e:
        print(False)
