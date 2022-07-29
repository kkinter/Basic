n = 3
li = [[0]*n for _ in range(n)]


# dir = [[0, 1],[1,
# 2차원 배열 생성
cnt = 1
dx = [0, 1, 2]
dy = [2, 1, 0]

for i in range(len(li)):
    for j in range(len(li[i])):
        li[(i) % 3][(j) % 3] = cnt 
        cnt += 1





for i in li:
    for j in i:
        print(j, end=' ')
    print()