from sys import stdout, stdin

input = stdin.read().splitlines()
output = []
mod = 10**9 + 7

n = int(input[0])
output.append(str(2**n % mod))

stdout.write("\n".join(output))
