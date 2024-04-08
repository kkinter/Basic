a, b = map(int, input().split())
arr = []
for x in range(1,b + 1):
    for j in range(1,x + 1):
        arr.append(x)
    
print(arr)
answer = 0

for j in arr[a-1:b]:
    answer += int(j)

print(answer)