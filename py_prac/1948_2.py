t = int(input())
li = [0,31,28,31,30,31,30,31,31,30,31,30,31]
li2 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(t):
    m1, d1, m2, d2 = map(int,input().split()) 
    
    sum_date1 = sum(li[1:m1]) + d1
    sum_date2 = sum(li[1:m2]) + d2
    
    

    print(f"#{i+1} {sum_date2-sum_date1+1}")