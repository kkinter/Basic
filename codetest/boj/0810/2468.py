from collections import deque
import sys
from pprint import pprint
sys.stdin = open('./2468.txt')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_val = 0
min_val = 101
for i in range(n):
    for j in range(n):
        max_val = max(max_val, matrix[i][j])
        min_val = min(min_val, matrix[i][j])

def bfs(x, y,stan):
    que = deque()
    que.append([x, y])
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue

            if matrix[nx][ny] <= stan:
                continue

            if matrix[nx][ny] > stan:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([nx, ny])
res = []
for l in range(min_val, max_val + 1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for p in range(n):
        for q in range(n):
            if matrix[p][q] > l and not visited[p][q]:
                bfs(p, q, l)
                cnt += 1
    res.append(cnt)
if not max(res):
    print(1)
else:
    print(max(res))
    

