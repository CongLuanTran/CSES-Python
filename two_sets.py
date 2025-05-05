from sys import stdout, stdin

input = stdin.read().splitlines()
n = int(input[0])
output = []

rem = n % 4

if not rem:
    output.append("YES")
    lst = list(range(1, n + 1))
    output.append(str(n // 2))
    a = lst[: n // 4] + lst[3 * n // 4 :]
    output.append(" ".join(map(str, a)))
    output.append(str(n // 2))
    b = lst[n // 4 : 3 * n // 4]
    output.append(" ".join(map(str, b)))
elif rem == 3:
    output.append("YES")
    lst = list(range(1, n + 1))
    output.append(str(n // 2 + 1))
    a = [1, 2] + lst[3 : (n - 3) // 4 + 3] + lst[3 * (n - 3) // 4 + 3 :]
    output.append(" ".join(map(str, a)))
    output.append(str(n // 2))
    b = [3] + lst[(n - 3) // 4 + 3 : 3 * (n - 3) // 4 + 3]
    output.append(" ".join(map(str, b)))
else:
    output.append("NO")


stdout.write("\n".join(output))
