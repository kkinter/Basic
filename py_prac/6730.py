t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    up_li =[]
    dn_li = []
    for j in range(len(arr)-1):
        gap = arr[j] - arr[j+1]
        if gap > 0:
            dn_li.append(gap)
        elif gap < 0:
            up_li.append(gap)
    if len(up_li) < 0:
        
    max_up = -1*min(up_li)
    max_down = max(dn_li)
    

    print(f"#{i+1} {max_up} {max_down}")
