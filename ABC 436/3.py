import sys
input = sys.stdin.readline

N, M = map(int, input().split())


arr = set()
ans = 0

for i in range(M):
    r, c = map(int, input().split())
    if (r, c) not in arr and (r+1, c) not in arr and (r, c+1) not in arr and (r+1, c+1) not in arr:
        arr.add((r, c))
        arr.add((r+1, c+1))
        arr.add((r+1, c))
        arr.add((r, c+1))
        ans+=1
    
print(ans) 
    