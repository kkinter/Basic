arr = []
for i in range(9):
    n = int(input())
    arr.append(n)

arr = sorted(arr)

start = 0
end = 1
while sum(arr[start:end]) != 100:
    if sum(arr[start:end]) < 100:
        end += 1
    elif sum(arr[start:end]) > 100:
        start += 1

for j in arr[start:end]:
    print(j)
    