# ruff: noqa: E731
from collections import deque
import math
import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
ni = lambda: int(next(it))
ns = lambda: next(it).decode()
out = []
write = lambda x: out.append(str(x))

n = ni()

grid = [[math.inf] * n for _ in range(n)]
qu = deque()

grid[0][0] = 0
visited = set()
visited.add((0, 0))
qu.append((0, 0))
pos = [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-2, 1), (-1, 2), (2, -1)]

while len(qu) > 0:
    coord = qu.popleft()
    for p in pos:
        c = tuple(x + y for x, y in zip(coord, p))
        if 0 <= c[0] < n and 0 <= c[1] < n and c not in visited:
            grid[c[0]][c[1]] = grid[coord[0]][coord[1]] + 1
            visited.add(c)
            qu.append(c)

for line in grid:
    write(" ".join(str(num) for num in line))
sys.stdout.write("\n".join(out) + "\n")
