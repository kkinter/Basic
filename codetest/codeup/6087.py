a = int(input())
cnt = 1
while cnt <= a:
    if cnt % 3 == 0:
        print("" ,end='')
        cnt += 1
    else:
        print(cnt, end=' ')
        cnt += 1


