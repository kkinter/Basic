
from pprint import pprint
import sys
sys.stdin = open('./4396.txt')

n = int(input())

matrix = [list(input()) for _ in range(n)]
info = [list(input()) for _ in range(n)]
arr = [[0]*n for _ in range(n)]

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '*':
            for k in dir:
                try:
                    nx = i + k[0]
                    ny = j + k[1]
                    if matrix[nx][ny] == '.' and nx >= 0 and ny >= 0:
                        arr[nx][ny] += 1
                except:
                    pass
is_break = False
for i in range(n):
    for j in range(n):
        if info[i][j] == 'x' and matrix[i][j] == '*':
            is_break = True
        
        if info[i][j] == 'x' and matrix[i][j] != '*':
            print(arr[i][j], end='')
        
        elif is_break == True:
            print(matrix[i][j], end='')

        elif is_break == False:
            print(info[i][j], end='')
    if i != n - 1:
        print()
    