
def bianry(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        
        if arr[mid] > target:
            end = mid - 1
        
        else: 
            start = mid + 1
    return None

n = int(input())
p_card = list(map(int, input().split()))
m = int(input())
f_card = list(map(int, input().split()))

dict = {}
for f in f_card:
    dict[f] = 0

rev = sorted(f_card)
rev_p = sorted(p_card)
for p in p_card:
    if bianry(rev, p, 0, len(rev) - 1):
        dict[p] += 1

for res in f_card:
    if bianry(rev_p, res, 0, len(rev_p) - 1):
        print(dict[res], end=' ')
    else:
        print(0, end=' ')
