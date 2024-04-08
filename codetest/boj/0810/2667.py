from collections import deque
import sys
from pprint import pprint
sys.stdin = open('./2667.txt')

n = int(input())
visited = [[False] * n for _ in range(n)]
matrix = [list(map(int,list(input()))) for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue

            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    cnt += 1
    return cnt

arr = []
count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] and not visited[i][j]:
            arr.append(bfs(i, j))
            count += 1
print(count)
arr = sorted(arr)
for l in arr:
    print(l)   


    