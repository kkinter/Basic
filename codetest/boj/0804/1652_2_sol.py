import sys


# sys.stdin = open('./1652.txt')

n = int(input())
arr = [list(input()) for _ in range(n)]
col_arr = [[0] * n for x in range(n)]

for i in range(n):
    for j in range(n):
        col_arr[i][j] = arr[j][i]

row = 0

for i in range(n):
    temp = ''
    for j in arr[i]:
        temp += j
    temp = temp.split('X')
    for k in temp:
        if len(k) > 1:
            row += 1

col = 0

for i in range(n):
    temp = ''
    for j in col_arr[i]:
        temp += j
    temp = temp.split('X')
    for k in temp:
        if len(k) > 1:
            col += 1


print(row, col)