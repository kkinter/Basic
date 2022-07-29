## 시간초과 >> input을 sys로 바꿨을 때, 통과하는 문제는 시간 복잡도를 맞게 한건가 ? 하는 의문이 드네
import sys
input = sys.stdin.readline
n = int(input())
arr = []
sum_val = 0

for i in range(n):
    num = int(input())
    arr.append(num)

    sum_val += num
    
arr = sorted(arr)
min_val = arr[0]
max_val = arr[-1]

dic = {}

for j in arr:
    if j not in dic:
        dic[j] = 0
    if j in dic:
        dic[j] += 1

max_key = max(dic.values())
ans = []
res = 0
for key, val in dic.items():
    if val == max_key:
        ans.append(key)

if len(ans) == 1:
    res = ans[0]
else:
    res = sorted(ans)[1]


mid = n // 2
print(f"{round(sum_val / n)}")
print(arr[mid])
print(res)
print(max_val - min_val)