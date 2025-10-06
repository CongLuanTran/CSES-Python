from sys import stdout, stdin

input = stdin.read().splitlines()
n = int(input[0])
output = []

"""
Explanation:
For two knights to attack each other, they must each be in the opposite corners
of a 2x3 block. So we can find the number of attackable possition, then deduce
that from all possible positions. To place a 2x3 block in a nxn square (n>=3),
we have (n-1)*(n-2) ways. But horizontal and vertical blocks are distinct,
so we double, 2*(n-1)*(n-2). For each such blocks, there are two positions that
two knights can attach each other. So, the total number of attackable positions
is 4*(n-1)*(n-2) for a nxn square.
"""
for i in range(1, n + 1):
    if i == 1:
        output.append(0)
    elif i == 2:
        output.append(6)
    else:
        places = i**2
        possible = places * (places - 1) // 2
        attackable = 4 * (i - 1) * (i - 2)
        output.append(possible - attackable)

stdout.write("\n".join(map(str, output)))
