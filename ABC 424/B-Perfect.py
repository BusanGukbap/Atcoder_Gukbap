import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

A = [0 for _ in range(N+1)]
ans = []

for i in range(K):
    a, b = map(int, input().split())
    
    A[a] |= (1<<(b-1))
    
    if A[a] == (1<<M)-1:
        ans.append(a)

print(' '.join(map(str, ans)))