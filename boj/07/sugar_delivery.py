n = int(input())
cnt = 0
while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        break
    elif n == 1 or n == 2:
        cnt = -1
        break
    n -= 3
    cnt += 1

print(cnt)

