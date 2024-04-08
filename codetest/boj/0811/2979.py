a, b, c = map(int, input().split())
sum_val = 0
arr = [0] * 101

for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        arr[j] += 1

print(arr.count(1) * a + arr.count(2) * b * 2 + arr.count(3) * c * 3)
