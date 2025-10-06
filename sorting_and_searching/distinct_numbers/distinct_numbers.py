from itertools import groupby
import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
ni = lambda: int(next(it))
ns = lambda: next(it).decode()
out = []
write = lambda x: out.append(str(x))

n = ni()
x = [ni() for _ in range(n)]
x.sort()
print(groupby(x))
write(sum(1 for _ in groupby(x)))

sys.stdout.write("\n".join(out) + "\n")
