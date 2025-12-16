import sys

input = sys.stdin.readline

N = int(input())
S = input().rstrip()
a = N-len(S)

ans = 'o'*a + S

print(ans)