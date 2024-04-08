import sys
sys.stdin = open('./1652.txt')

n = int(input())
arr = [list(input()) for _ in range(n)]


row = 0

for i in range(n):
    temp = 0
    for j in range(1, n):
        if arr[i][j] != 'X' and arr[i][j - 1] != 'X':
            temp = 1
        
    row += temp
    
col = 0   

for i in range(n):
    temp = 0
    for j in range(1, n):
        if arr[j][i] != 'X' and arr[j - 1][i] != 'X':
            temp += 1
    if temp > 0:
        col += 1

print(row, col)