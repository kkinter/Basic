t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    li = [0 for _ in range(n)] # 빈 리스트 선언 1차원 배열
    
    for j in range(n):
        li[j] = list(map(int,input().split())) # 1차원 배열에 리스트 배열 > 2차원 배열
    
    print(li,li[0][2])

