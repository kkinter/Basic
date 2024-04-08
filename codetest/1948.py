t = int(input())
li = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(t):
    m1, d1, m2, d2 = map(int,input().split())
    num1 = 0
    num2 = 0
    
    sum_date1 = 0
    sum_date2 = 0
    for j in range(1,m1+1):
        sum_date1 += li[j] 
    sum_date1 += d1
    for k in range(1,m2+1):
        sum_date2 += li[k] 
    sum_date2 += d2
    print(f"#{i+1} {sum_date2-sum_date1+1}")