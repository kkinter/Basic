def binary(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    return None    

n = int(input())
p_arr = list(map(int, input().split()))
m = int(input())
f_arr = list(map(int, input().split()))

li = [0] * m
f_arr_sort = sorted(f_arr)  ## 이진 탐색을 위해서 arr 정렬  = O(N)
for p in p_arr:   # O(N)
    if binary(f_arr_sort, p, 0, len(f_arr) - 1): # O(logN)
        li[f_arr.index(p)] += 1 # 결과 값은 정렬되기 전의 인덱스 값으로 > # > O(N)

for i in li:
    print(i, end=' ')

## N^2logN ? 