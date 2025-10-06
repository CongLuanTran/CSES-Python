from sys import stdout, stdin

input = stdin.read().splitlines()
output = []

for line in input[1:]:
    a, b = map(int, line.split())
    if (a + b) % 3 != 0 or a > 2 * b or b > 2 * a:
        output.append("NO")
    else:
        output.append("YES")

stdout.write("\n".join(output))
