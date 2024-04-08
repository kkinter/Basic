import heapq
import sys

input = sys.stdin.readline

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

heap = []

for number in numbers:
    if number != 0:
        heapq.heappush(heap, (abs(number), number))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    