from collections import deque
from itertools import count
import sys
from pprint import pprint

sys.stdin = open('./1926.txt')

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    global count
    que = deque()
    que.append([x, y])
    arr[x][y] = 1
    

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                if matrix[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    que.append([nx, ny])
                    count += 1
    
    return count
cnt = 0
res = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not arr[i][j]:
            count = 1
            res.append(bfs(i, j))
            cnt += 1
if cnt == 0:
    print(0)
    print(0)
else:
    print(cnt)
    print(max(res))