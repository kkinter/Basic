n = int(input())

for i in range(1,n+1):
    new_str = ''
    li = []
    cnt = 0
    for j in str(i):
        if int(j) % 3 == 0 and int(j) != 0:
            new_str = '-'
            cnt += 1
            if cnt > 1:
                new_str += '-'
        elif cnt == 1:
            new_str = '-'
        else:
            new_str += j 
        
    if i != n:
        print(new_str,end=" ")
    else:
        print(new_str,end='')