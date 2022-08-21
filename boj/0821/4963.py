from collections import deque
import sys
from pprint import pprint
sys.stdin = open('./4963.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    que = deque()
    que.append([x, y])
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    que.append([nx, ny])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * (w) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j)
    print(cnt)
    
