import sys

input = sys.stdin.readline

N = int(input())

s = set()
s.add(N)

while N != 1:
    temp = 0
    cur = N
    
    while N:
        temp += (N % 10)**2
        N //= 10
    if temp in s:
        print("No")
        sys.exit(0)
    
    s.add(temp)
    N = temp
    
print("Yes")