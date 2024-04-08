a = int(input())
cnt = 1
while cnt <= a:
    if cnt % 10 == 3 or cnt % 10 == 6 or cnt % 10 == 9  :
        print("X", end=' ')
        cnt += 1
    else:
        print(cnt, end=' ')
        cnt += 1


