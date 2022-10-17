# https://www.acmicpc.net/problem/11057
# f(1) = 10 
n = int(input())
cnt = 0
for i in range(0, 10**n):
    str_i = str(i)
    
    if "".join(sorted(str_i)) == str_i:
        cnt += 1
print(cnt)
        

# 10, 55, 220, 715, 2002, 5005 