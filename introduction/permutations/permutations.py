from sys import stdin, stdout

input = stdin.read()
n = int(input)

if n < 4 and n > 1:
    stdout.write("NO SOLUTION")
else:
    li = [x for x in range(n - 1, 0, -2)] + [x for x in range(n, 0, -2)]
    stdout.write(" ".join(map(str, li)))
