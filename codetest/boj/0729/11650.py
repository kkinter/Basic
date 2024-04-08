import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    coor = list(map(int, sys.stdin.readline().split()))
    arr.append(coor)

arr = sorted(arr) # > NlogN

for j in arr: # N
    print(" ".join(map(str, j))) # ? 