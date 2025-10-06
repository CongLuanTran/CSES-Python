from collections import Counter
from sys import stdin, stdout

input = stdin.read()

d = Counter(input.strip())

center = ""
right = ""
left = ""

for k, v in d.items():
    if v % 2 == 1:
        if len(center) == 0:
            center = k
        else:
            output = "NO SOLUTION"
            break
    left += k * (v // 2)
    right = k * (v // 2) + right
else:
    output = left + center + right

stdout.write(output)
