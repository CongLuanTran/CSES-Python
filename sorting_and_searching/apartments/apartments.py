import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
ni = lambda: int(next(it))
ns = lambda: next(it).decode()
out = []
write = lambda x: out.append(str(x))

n = ni()
m = ni()
k = ni()
a = [ni() for _ in range(n)]
b = [ni() for _ in range(m)]
a.sort()
b.sort()

i = 0
j = 0
res = 0
while i < len(a) and j < len(b):
    if a[i] > b[j] + k:
        j += 1
    elif a[i] < b[j] - k:
        i += 1
    else:
        res += 1
        i += 1
        j += 1

write(res)
sys.stdout.write("\n".join(out) + "\n")
