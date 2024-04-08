
#시간초과

t= int(input())

for i in range(1,t+1):
    n = int(input())
    li = list(map(int,input().split()))

    sum_val = 0
    length = len(li)
    cnt = 0
    while cnt <= len(li)-1:
        max_val = max(li[cnt:len(li)])
        if li[cnt] < max_val:
            sum_val += max_val-li[cnt]
        cnt += 1

    print(f"#{i} {sum_val}")