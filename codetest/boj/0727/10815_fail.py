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
n2 = int(input())
numbers2 = list(map(int, input().split())) # 입력 
check_num = [0 for x in range(len(numbers2))] # 존재 여부 리스트

numbers2.sort()

for j in range(len(numbers2)): # 0  
    if binary_search(numbers, numbers2[j], 0, len(numbers) - 1):
        print(numbers2[j],"가 있네요")
        check_num[j] += 1
    else:
        print(numbers2[j], "가 없네요")

print(" ".join(map(str,check_num)).rstrip())