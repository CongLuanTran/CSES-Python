import sys

input = sys.stdin.read()

n = int(input.splitlines()[0])


def solve(li, n):
    li.append(n)
    if n == 1:
        return li
    elif n & 1:
        return solve(li, n * 3 + 1)
    else:
        return solve(li, n // 2)


sys.stdout.write(" ".join(map(str, solve([], n))))
