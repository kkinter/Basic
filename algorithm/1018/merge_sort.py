"""
병합 정렬 (merge sort)
- 재귀용법을 활용한 정렬 알고리즘
- 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
- 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다. 
"""

def split(data):
    medium = int(len(data) // 2)
    left = data[:medium]
    right = data[medium:]
    print(left, right)

data_list = [3, 4, 1, 3, 2]
split(data_list)

def merge(left, right):
    merged = []
    left_point, right_point = 0, 0

    # case1: left/right 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1
    # case2: left만 남아있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
    
    # case3: right만 남아있을 때
    while len(right) > right_point:
        merged.append(right_point[right_point])
        right_point += 1
    
    return merged
def merge_split(data):
    if len(data) == 1:
        return data
    
    medium = int(len(data) // 2)
    left = merge_split(data[:medium])
    right = merge_split(data[medium:])
    return merge(left, right)

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr