"""
이진탐색
- 
"""

def b_search(arr, search):
    if len(arr) == 1 and arr[0] == search:
        return True
    elif len(arr) == 1 and arr[0] != search:
        return False
    elif len(arr) == 0:
        return False

    mid = len(arr // 2)
    if search == arr[mid]:
        return True
    else:
        if search > arr[mid]:
            return b_search(arr[:mid], search)
        else:
            return b_search(arr[mid:], search)

