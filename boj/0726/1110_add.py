n = int(input())
if n < 10:
    n *= 10
sum_val = 0
for i in str(n):
    sum_val += int(i)

new_num = n % 10 * 10 + sum_val % 10

cnt = 1
while new_num != n:
    sum_value = 0
    for j in str(new_num):
        sum_value += int(j)    
    new_num = new_num % 10 * 10 + sum_value % 10
    cnt += 1
print(cnt)