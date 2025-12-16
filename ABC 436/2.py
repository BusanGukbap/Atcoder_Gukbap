import sys

input = sys.stdin.readline

N = int(input())

arr = [0] * (N*N+1)

arr[(N-1)//2] = 1

r = 0
c = (N-1)//2
for i in range(1, N*N):
    a = (r-1)%N
    b = (c+1)%N
    if arr[a*N+b] == 0:
        arr[a*N+b] = i+1
        r = a
        c = b
    else:
        r = (r+1)%N
        arr[r*N+c] = i+1

for i in range(N):
    print(*arr[i*N:i*N+N])
    
