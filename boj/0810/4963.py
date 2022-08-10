import sys
from pprint import pprint
sys.stdin = open('./4963.txt')
input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, 1, -1,-1] # 8 방향
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= h or ny >= w or nx < 0 or ny < 0:
            continue

        if matrix[nx][ny] == 0:
            continue

        if matrix[nx][ny] == 1:
            if not visited[nx][ny]:
                dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]

    visited = [[False] * (w) for _ in range(h)]
    cnt = 0
    for j in range(h):
        for k in range(w):
            if matrix[j][k] == 1 and not visited[j][k]:
                dfs(j, k)
                cnt += 1 
    print(cnt)


    
        
