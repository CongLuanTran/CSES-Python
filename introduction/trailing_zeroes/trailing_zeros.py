from sys import stdout, stdin

input = stdin.read().splitlines()

n = int(input[0])
count = 0
i = 5
while n // i > 0:
    count += n // i
    i *= 5

stdout.write(str(count))
