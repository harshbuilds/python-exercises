# Find first alphanumeric character to be repeated consecutively
import re
pattern = r'([A-Za-z0-9])\1'
match = re.search(pattern, input())
if match:
    print(match.group(1))
else:
    print(-1)
