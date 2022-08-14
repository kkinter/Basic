from collections import deque
import sys
from pprint import pprint

sys.stdin = open("_등산로조성.txt")
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    stk = deque([[x, y]])
    arr[x][y] = 1
    flag = False
    while stk:
        x, y = stk.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if matrix[nx][ny] < matrix[x][y]:
                arr[nx][ny] = arr[x][y] + 1
                stk.append([nx, ny])

            if flag:
                matrix[x][y] = tmp

            if matrix[nx][ny] >= matrix[x][y]:
                for j in range(1, dep + 1):
                    if matrix[nx][ny] - j >= 0:
                        tmp = matrix[nx][ny]
                        flag = True
                        matrix[nx][ny] -= j
                        stk.append([nx, ny])


t = int(input())
for i in range(t):
    n, dep = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    max_val = 0
    for j in range(n):
        for k in range(n):
            max_val = max(max_val, matrix[j][k])  # 최대 봉우리 높이
   
    res = 0
    for j in range(n):
        for k in range(n):
            if matrix[j][k] == max_val:           # matrix의 요소가 최대 봉우리라면
                arr = [[0] * n for _ in range(n)]
                dfs(j, k)
                pprint(arr)
                


                