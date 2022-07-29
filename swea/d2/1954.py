
n = 4 
li = [[0]*n for _ in range(n)]
cnt = 1
x, y = 0 , 0
# dir = [[0, 1],[1, 0],[0, -1],[-1, 0]]
# dir_cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_cnt = 0
while cnt < n*n :
    if abs(x) == n - 1 or abs(y) == n - 1:
        dir_cnt += 1
        if dir_cnt == 4:
            dir_cnt = 0 
        x = x + dx[dir_cnt]
        y = y + dy[dir_cnt]
        print("1 조건문", x, y, cnt)
        cnt += 1

    if li[x][y] == False:
        li[x][y] = cnt
        x = x + dx[dir_cnt]
        y = y + dy[dir_cnt]
        print("2 조건문",x, y, cnt)
        cnt += 1
    
    elif li[x][y] :
        
        dir_cnt += 1
        if dir_cnt == 4:
            dir_cnt = 0 
        x = x + dx[dir_cnt]
        y = y + dy[dir_cnt]
        print("3 조건문", x, y, cnt)
        cnt += 1
    
print(li)