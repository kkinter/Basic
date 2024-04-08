from collections import deque
import sys
sys.stdin = open('./9205.txt')
t = int(input())

dx = [1, 0]
dy = [0, 1]


def bfs(x, y, p, q):
    que = deque()
    que.append([x, y])
    visted[x][y] = True
    arr = [[0] * p for _ in range(q)]
    
    if p == 0 or q == 0:
        return max(p, q)

    while que:
        x, y = que.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= q or ny >= q or nx < 0 or ny < 0:
                continue

            if not visted[nx][ny]:
                visted[nx][ny] = True
                arr[nx][ny] = arr[x][y] + 1

    return arr[p - 1][q - 1]

for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    for _ in range(n):
        store_x, store_y = map(int, input().split())
        visted = [[False] * (store_x // 50) for _ in range(store_y // 50)]
        print(visted)
        # bfs(home_x // 50, home_y // 50, store_x // 50, store_y // 50)
    fes_x, fes_y = map(int, input().split())

    
    

