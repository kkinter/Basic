import sys
t= int(sys.stdin.readline())

for i in range(1,t+1):
    n = int(sys.stdin.readline())
    li = list(map(int,sys.stdin.readline().split()))

    sum_val = 0
    length = len(li)
    cnt = 0
    while cnt <= len(li)-1:
        max_val = max(li[cnt:len(li)])
        if li[cnt] < max_val:
            sum_val += max_val-li[cnt]
        cnt += 1

    print(f"#{i} {sum_val}")