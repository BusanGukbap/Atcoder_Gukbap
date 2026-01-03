import sys
import math

input = sys.stdin.readline

N = int(input())

counts = bytearray(N + 1)
sqrt_num = math.isqrt(N // 2) + 1

for i in range(1, sqrt_num):
    i2 = i * i
    max_j = math.isqrt(N - i2)
    for j in range(i + 1, max_j + 1):
        counts[i2 + j * j] += 1

ans = [k for k, v in enumerate(counts) if v == 1]

print(len(ans))
print(*ans)