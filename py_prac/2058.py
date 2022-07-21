s = int(input())
sum_val =0
while s >= 1:
    sum_val += s % 10 
    s //= 10
print(sum_val)
