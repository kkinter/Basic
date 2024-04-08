
t = int(input())
for case in range(t):
    n = int(input())
    li = [[0]*n for _ in range(n)]


    length = n*n
    x = y = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir_cnt = 0
    cnt = 1
    while length + 1 > cnt:
        if x == n or y == n or x < 0 or y < 0 or li[x][y] != 0:
            x = x - dx[dir_cnt % 4] 
            y = y - dy[dir_cnt % 4]
            dir_cnt += 1

        
        else:
            li[x][y] = cnt
            cnt += 1

        x = x + dx[dir_cnt % 4] 
        y = y + dy[dir_cnt % 4]   

    print(f"#{case + 1}")    
    for i in li:
        for j in i:
            if j != i[-1]:
                print(j, end=' ')
            else:
                print(j, end='')
        print()
    
    

    


