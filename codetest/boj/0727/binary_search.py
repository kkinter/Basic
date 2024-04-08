def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return array[mid]
        
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1

    return None


binary_search([10, 9, -5, 2, 3, 4, 5, -10], 6, 0, 7)