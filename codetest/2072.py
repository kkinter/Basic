t = int(input())
for i in range(t):
    sum_val = 0
    s = list(map(int,input().split()))
    for j in s:
        if j % 2 == 1:
            sum_val += j

    print(f"#{i+1} {sum_val}")