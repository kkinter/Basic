t = int(input())
for q in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if n > m:
        gap = n-m
        li = []
        for i in range(gap+1):
            sum_val = 0
            for j in range(m):
                sum_val += b[j] * a[j+i]
            li.append(sum_val)
        print(f"#{q+1} {max(li)}")
        
    elif n < m:
        gap = m-n
        li = []
        for i in range(gap+1):
            sum_val = 0
            for j in range(n):
                sum_val += a[j]*b[j+i]
            li.append(sum_val)
        print(f"#{q+1} {max(li)}")
    else:
        li = []
        for i in range(n):
            sum_val=0
            for j in range(m):
                sum_val += a[j]*b[j]
            li.append(sum_val)
        print(f"#{q+1} {max(li)}")
            
            
            
