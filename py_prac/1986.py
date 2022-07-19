t = int(input())
for i in range(t):
    a = int(input())
    sum_val = 0    
    for j in range(1,a +1):
        if j % 2 == 0:
            sum_val -= j
        if j % 2 == 1:
            sum_val += j
    print(f"#{i+1} {sum_val}")
