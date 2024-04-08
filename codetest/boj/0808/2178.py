import sys
sys.stdin = open('./2178.txt')


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x = 0
y = 0

cnt = 0
while True:
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if matrix[ny][nx] == '1':
            x = nx
            y = ny
            
            cnt += 1
        print(x, y)
    if x == m - 1 and y == n - 1:
        break
    
    
            