n = int(input())

for i in range(1,n+1):
    new_str = ''
    cnt = 0
    for j in str(i):
        if int(j) % 3 == 0 and int(j) != 0:
            cnt += 1
        else:
            new_str += j
    if cnt > 0:
        print(cnt*"-",end=" ")
    else:
        print(new_str,end=" ")
   