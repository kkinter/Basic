t = int(input()) # 10
for i in range(t):
    n =int(input()) # 5
    for j in range(n):
        temp_li = list(map(int,input().split())) # 1 4 7 8 0
        length = len(temp_li)
        for k in range(length-1):
            for q in range(length-k-1):
                if temp_li[q] > temp_li[q+1]:
                    temp_li[q], temp_li[q+1] = temp_li[q+1], temp_li[q]      
        print(f"#{i+1} {temp_li}")