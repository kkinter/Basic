t = int(input())
for i in range(t):
    start, end = map(int, input().split())
    zero_cnt = 0
    for j in range(start, end + 1):
        for k in str(j):
            if '0' in k:
                zero_cnt += 1
    print(zero_cnt)