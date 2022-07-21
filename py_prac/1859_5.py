from curses import init_pair


t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    max_val = s[-1]
    sum_val = 0
    for j in range(len(s)-2,-1,-1):
        if s[i] < max_val:
            sum_val += max_val-s[i]
        elif s[i] > max_val:
            max_val = s[i]
    print(f"#{i+1} {sum_val}")