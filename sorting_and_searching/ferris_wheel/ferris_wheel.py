import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
ni = lambda: int(next(it))
ns = lambda: next(it).decode()
out = []
write = lambda x: out.append(str(x))

n = ni()
x = ni()
p = [ni() for _ in range(n)]
p.sort()
l = 0
r = n - 1
count = 0
while l <= r:
    count += 1
    if l == r:
        break
    if p[l] + p[r] <= x:
        l += 1
    r -= 1

write(count)

sys.stdout.write("\n".join(out) + "\n")
