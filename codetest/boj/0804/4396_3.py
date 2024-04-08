
from pprint import pprint
import sys
sys.stdin = open('./4396.txt')

n = int(input())

matrix = [list(input()) for _ in range(n)]
info = [list(input()) for _ in range(n)]
arr = [[0]*n for _ in range(n)]
pprint(matrix)
pprint(info)
pprint(arr)
for i in range(n - 1):
    for j in range(n - 1):
        if matrix[i][j] == '.':
            
            
