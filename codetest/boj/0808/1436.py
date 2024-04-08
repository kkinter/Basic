n = int(input())
# 666, 1666, 2666, 3666, 4666, 5666
cnt = 1
for i in range(10000000):
    if '666' in str(i):
        if cnt == n:
            print(i)
        cnt += 1