k = int(input())
for _ in range(1, k + 1):
    arr = sorted(list(map(int, input().split())), reverse= True)
    gap = 100
    for i in range(len(arr) - 2):
        gap = min(gap, arr[i + 1] - arr[i]) 
    
    max_val = max(arr[:-1])
    min_val = min(arr[:-1])
    print(f'Class {_}')
    print(f'Max {max_val}, Min {min_val}, Largest gap {abs(gap)}')
