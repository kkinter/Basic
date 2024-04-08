import sys
sys.stdin = open('./2592.txt')
dic = {}
for i in range(10):
    num = int(input())
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1
max_val = max(dic.values())

sum_val = 0
fre = 0
for key , val in dic.items():
    sum_val += key * val
    if val == max_val:
        fre = key

print(sum_val // 10, fre)

