t = int(input())
for i in range(t):
    cnt = 1
    ycnt = 0
    kcnt = 0 
    for j in range(9):
        y, k = map(int,input().split())
        if y > k :
            ycnt += 1
        elif k < y:
            kcnt += 1
    if ycnt > kcnt:
        print('Yonsei')
    elif ycnt == kcnt:
        print('Draw')
    else:
        print('Korea')