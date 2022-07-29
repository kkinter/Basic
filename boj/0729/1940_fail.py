import sys
input = sys.stdin.readline

n = int(input())    
m = int(input())
numbers = list(map(int, input().split()))
cnt = 0
numbers = sorted(numbers, reverse= True)

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] + numbers[j] == m:
            cnt += 1

print(cnt)