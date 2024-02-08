# Create a regex pattern which will be used to split the currency by , and .

regex_pattern = r"[,\.](?=\d+)"

import re
print("\n".join(re.split(regex_pattern, input())))
