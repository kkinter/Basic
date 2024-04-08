k = int(input())
for _ in range(1, k + 1):
    arr = list(map(int, input().split()))
    arr.pop(0)
    arr = sorted(arr)
    gap = 0
    for i in range(len(arr) - 1):
        gap = max(gap ,arr[i + 1] - arr[i])
    max_val = max(arr)
    min_val = min(arr)
    print(f'Class {_}')
    print(f'Max {max_val}, Min {min_val}, Largest gap {abs(gap)}')
