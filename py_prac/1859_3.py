t= int(input())

for i in range(1,t+1):
    n = int(input())
    li = list(map(int,input().split()))
    max_val = max(li)
    sum_val = 0
    length = len(li)
    cnt = 0
    while cnt < length-1:
        if li[cnt] == max_val:
            max_val = max(li[cnt+1:])
        else:
            sum_val += max_val - li[cnt]
        cnt += 1
    print(f"#{i} {str(sum_val)}")


    