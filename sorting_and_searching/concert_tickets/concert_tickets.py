import bisect
import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
ni = lambda: int(next(it))
ns = lambda: next(it).decode()
out = []
write = lambda x: out.append(str(x))
upper_bound = bisect.bisect_right
lower_bound = bisect.bisect_left

n = ni()
m = ni()
h = [ni() for _ in range(n)]
t = [ni() for _ in range(m)]
h.sort()

for ti in t:
    idx = upper_bound(h, ti)
    if idx > 0:
        write(h[idx - 1])
        h.pop(idx - 1)
    else:
        write("-1")

sys.stdout.write("\n".join(out) + "\n")
