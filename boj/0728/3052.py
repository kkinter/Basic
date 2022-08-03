def div_42(n):
    return n % 42

arr =[]
for i in range(10):
    n = int(input())
    arr.append(n)
remain = set()
for num in map(div_42, arr):
    remain.add(num)

print(len(remain))