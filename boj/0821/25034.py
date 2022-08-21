x = int(input())
n = int(input())
sum_val = 0
for i in range(n):
    a, b = map(int, input().split())
    sum_val += a * b

if sum_val == x:
    print('Yes')
else:
    print('No')