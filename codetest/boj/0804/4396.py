
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
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '*':
            try:
                arr[i - 1][j - 1] += 1 # 우측 상단
            except:
                pass
            try:    
                arr[i - 1][j] += 1 # 우측
            except:
                pass    
            try:    
                arr[i - 1][j + 1] += 1 # 우측 하단
            except:
                pass
            try:    
                arr[i][j - 1] += 1 # 하단
            except:
                pass    
            try:    
                arr[i][j + 1] += 1 # 상단
            except:
                pass    
            try:    
                arr[i + 1][j - 1] += 1 # 좌측 상단
            except:
                pass   
            try:
                arr[i + 1][j] += 1# 좌측
            except:
                pass    
            try:    
                arr[i + 1][j + 1] += 1# 좌측 하단
            except:
                pass
pprint(arr)