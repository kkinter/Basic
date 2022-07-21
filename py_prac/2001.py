t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    li = [0 for _ in range(n)] # 빈 리스트 선언 1차원 배열
    for j in range(n):
        li[j] = list(map(int,input().split())) # 1차원 배열에 리스트 배열 > 2차원 배열
    sum_list = []
    gap = n-m
    cnt = 0
    
    for g in range(1,gap+1):
        sum_val = 0
        for w in range(g,gap):
            for h in range(g,gap):
                sum_val += li[w][h]
                cnt += 1
                print(w,h)
        
            sum_list.append(sum_val)

    print(sum_list,cnt)
                 
