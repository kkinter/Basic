# 시간 초과
# 2초 >> 2억번의 연산 ?
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    k = int(input())
    arr.append(k)

arr_sort = sorted(arr)
res = []
length = len(arr_sort)
for j in range(length): # 100,000 
    res.append(arr_sort[j] * (length - j))

print(max(res))

# print(min(arr) * n) # case 1 1 1 1 100 >> fail
# case 가 뭐가 있을까 
# 1 1 1 1 100
# 10 20 30 40 
# 모든 리스트를 순회해서 min 값의 * length 를 하면 될듯?

## > list[::] 이 생각보다 비용이 크다