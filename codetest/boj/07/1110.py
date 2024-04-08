n = int(input())
cnt = 0
temp = n
result = 0
while True:
    result = (temp % 10)*10 + (temp//10 + temp%10) % 10
    if result != n:
        temp = result
        cnt += 1
    elif result == n:
        break

print(cnt+1)