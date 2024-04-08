
import sys 
input = sys.stdin.readline
n = int(input())
arr = []
interval = {}
for i in range(n):
    arr.append(int(input()))
    
arr = sorted(arr)

interval = {}
for j in range(len(arr) - 1): # n ^ 2 아님? 
    diff = arr[j + 1] - arr[j]
    if diff not in interval:
        interval[diff] = 0
    if diff in interval:
        interval[diff] += 1

ans = 0
min_diff = min(interval.keys())
for key, val in interval.items():
    if key != min_diff:
        ans += ((val * key) // min_diff) - 1
    
print(ans, interval, min_diff)
## 최대 공약수 
def gcd(arr):
    