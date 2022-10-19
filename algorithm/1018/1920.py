import sys
sys.setrecursionlimit(10**7)
arr1 = [4, 1, 5, 2, 3]
arr1 = sorted(arr1)

def func(val, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2
    
    if val > arr1[mid]:
        return func(val, mid + 1, end)
    elif val < arr1[mid]:
        return func(val, start, mid - 1)
    else:
        return True
    


def b_search(arr, search):
    if len(arr) == 0 and search == arr[0]:
        return 1
    elif len(arr) == 0 and search != arr[0]:
        return 0
    elif len(arr) == 0:
        return 0

    mid = len(arr) // 2

    if search == arr[mid]:
        return 1
    else:
        if search > arr[mid]:
            return b_search(arr[mid:], search)
        else:
            return b_search(arr[:mid], search)


arr2 = [1, 3, 7, 9, 5]

for i in arr2:
    if func(i, 0, len(arr1) - 1):
        print(1)
    else:
        print(0)

  