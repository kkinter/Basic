## 시간 제한 2초
## 입력 500,000  n^2 은 안되겠네
## 구현한 코드 O(n^2)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1

    return None




n = int(input())
numbers = list(map(int, input().split()))
m= int(input())
numbers2 = list(map(int, input().split()))
check_num = [0 for x in range(m)]
for num in range(n):
    if binary_search(numbers2, numbers[num], 0, len(numbers2) - 1):
        check_num[numbers[num]] += 1
print(check_num)