t = 10
for i in range(t):
    n = int(input())
    n, m = map(int,input().split())
    cnt = 1
    res = n
    while cnt < m:
        res *= n 
        cnt += 1
    print(f"#{i+1} {res}")