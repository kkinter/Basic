import sys

# sys.stdin = open("./1236.txt")

n, m = map(int, input().split())
arr = [list(input()) for x in range(n)]


col = []

for i in range(m):
    is_in = False
    for j in range(n):
        if arr[j][i] == 'X':
            is_in = True
    if is_in:
        col.append('X')
    else:
        col.append('0')

row = []

for i in range(n):
    is_in = False
    for j in range(m):
        if arr[i][j] == 'X':
            is_in = True
    
    if is_in:
        row.append('X')
    else:
        row.append('0')


print(max(row.count('0') , col.count('0')))

    

        
        