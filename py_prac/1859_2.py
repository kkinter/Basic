

t= int(input())

for i in range(1,t+1):
    n = int(input())
    li = list(map(int,input().split()))
    max_val = max(li)
    sum_val = 0
    length = len(li)
    for j in range(len(li)):
        max_val = max(li[j:len(li)])
        if j < max_val:
            sum_val += max_val - j
        
    

    print(f"#{i} {sum_val}")