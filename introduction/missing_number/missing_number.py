from sys import stdout, stdin

input = stdin.read()
n, num = input.splitlines()

n = int(n)
s1 = {x for x in range(1, n + 1)}
s2 = set(map(int, num.split()))
stdout.write(str(list((s1 - s2))[0]))
