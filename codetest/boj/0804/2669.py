import sys
# from pprint import pprint

# sys.stdin = open('./2669.txt')

matrix = [list(map(int, input().split())) for _ in range(4)]
col = [[0]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        col[i][j] = matrix[j][i]

max_x = max(col[2])
min_x = min(col[0])

max_y = max(col[3])
min_y = min(col[1])

arr = [[0] * max_x for _ in range(max_y)]

for coor in range(4):
    i, j, x, y = matrix[coor][0], matrix[coor][1], matrix[coor][2], matrix[coor][3]
    
    for j in range(j, y):
        for k in range(i, x):
            arr[j][k] = 1

sum_val = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum_val += arr[i][j]

print(sum_val)
