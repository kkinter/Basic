import heapq

n = int(input())
arr = []
heap = []
for i in range(n):
    num = int(input())
    arr.append(num)

for j in arr:
    heapq.heappush(heap, j)

while heap:
    print(heapq.heappop(heap))