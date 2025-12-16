import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())

arr = list(input().rstrip() for _ in range(H))
visited = [[0]*W for _ in range(H)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0, 0, 0))
visited[0][0] = 1

portal = dict()

for i in range(H):
    for j in range(W):
        temp = arr[i][j]
        # print(temp)
        if 'a' <= temp <= 'z':
            if temp not in portal:
                portal[temp] = []
            portal[temp].append((i, j))

ans = 0
alphabet = dict()
while q:
    cnt, cy, cx = q.popleft()
    
    if cy == (H-1) and cx == (W-1):
        ans = cnt
        break
    
    if 'a' <= arr[cy][cx] <= 'z' and arr[cy][cx] not in alphabet:
        temp = arr[cy][cx]
        for a, b in portal[temp]:
            if visited[a][b] == 1:
                continue
            q.append((cnt+1, a, b))
            visited[a][b] = 1
        alphabet[temp] = 1
        
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if nx < 0 or ny < 0 or nx >= W or ny >= H or visited[ny][nx] == 1:
            continue
        elif arr[ny][nx] == '#':
            visited[ny][nx] = 1
            continue
        else:
            visited[ny][nx] = 1
            q.append((cnt+1, ny, nx))

if visited[H-1][W-1] == 1:
    print(ans)
else:
    print(-1)