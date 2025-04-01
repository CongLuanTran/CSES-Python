from sys import stdin, stdout

input = stdin.read()
x = list(map(int, input.splitlines()[1].split()))

m = 0
c = 0

for n in x:
    m = max(m, n)
    c += m - n

stdout.write(str(c))
