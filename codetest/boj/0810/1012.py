from collections import deque
import sys
from pprint import pprint

sys.stdin = open('./1012.txt')

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    que = deque()
    que.append([x,y])
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            if adj_matrix[nx][ny] == 0:
                continue

            if adj_matrix[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([nx, ny])
    

for i in range(t):
    m, n, k = map(int, input().split())
    adj_matrix = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for j in range(k):
        x, y = map(int, input().split())
        adj_matrix[y][x] = 1
    
    cnt = 0 
    for q in range(n):
        for p in range(m):
            if adj_matrix[q][p] == 1 and not visited[q][p]:
                cnt += 1
                bfs(q, p)
                
    print(cnt)
