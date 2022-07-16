## 자릿수 계산
from unittest import result


s = '156'
sum_val = 0
for i in s:
    sum_val += int(i)

print(sum_val)

def cal():
    cnt = 1
    results = 0
    if cnt == 10000:
        return 1
    for i in str(cnt):
        results += i
    results += cnt

