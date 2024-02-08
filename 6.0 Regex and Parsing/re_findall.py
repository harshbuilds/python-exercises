# Find all subtrings containing 2 or more vowels surrounded by consonants
# String can contain all alphabets and symbols (+- )
import re

line = input()
match = re.findall(r'(?<=[b-df-hj-np-tv-z])[aeiou]{2,}(?=[b-df-hj-np-tv-z])', line, flags=re.IGNORECASE)
if len(match):
    print(*match, sep="\n")
else:
    print(-1)
