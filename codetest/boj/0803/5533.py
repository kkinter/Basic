import sys
# sys.stdin = open('./5533.txt')

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]

board = [0]*n
arr = []
for i in range(3):
    temp = []
    for j in range(n):
        temp.append(score[j][i])
    arr.append(temp)
    
for i in range(n):
    for j in range(3):
        if arr[j].count(arr[j][i]) >= 2:  # [[100, 100, 63, 99, 89], [99, 97, 89, 99, 97], [98, 92, 63, 99, 98]]
            board[i] -= arr[j][i]        

for i in range(3):
    for k in range(n):
        board[k] += score[k][i]

for res in board:
    print(res)