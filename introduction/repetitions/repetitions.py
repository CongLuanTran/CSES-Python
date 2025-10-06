from sys import stdin, stdout

input = stdin.read()

letter = ""
length = 0
longest = 0

for c in input:
    if c != letter:
        length = 0
        letter = c
    length += 1
    longest = max(longest, length)

stdout.write(str(longest))
