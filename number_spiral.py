from sys import stdin, stdout

input = stdin.read().splitlines()
output = []
for line in input[1:]:
    y, x = list(map(int, line.split()))
    if y > x:
        botleft = (y - 1) ** 2 + 1 if y & 1 else y**2
        shift = (x - 1) * (1 if y & 1 else -1)
        output.append(botleft + shift)
    else:
        topright = x**2 if x & 1 else (x - 1) ** 2 + 1
        shift = (y - 1) * (-1 if x & 1 else 1)
        output.append(topright + shift)

stdout.write("\n".join(map(str, output)))
