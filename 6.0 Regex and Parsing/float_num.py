# Match a floating point number
import re
pattern = re.compile(r'([+-]?[0-9]*)?\.[0-9]+')
for _ in range(int(input())):
    print(True if re.fullmatch(pattern, input()) else False)

