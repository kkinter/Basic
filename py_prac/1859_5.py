
t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    max_val = s[-1]
    sum_val = 0
    for j in range(len(s)-2,-1,-1):
        if s[j] < max_val:
            sum_val += max_val-s[j]
        elif s[j] > max_val:
            max_val = s[j]
    print(f"#{i+1} {sum_val}")