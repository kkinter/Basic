
arr = [f"{str(x)*x}" for x in range(1, 50)]
add_arr =''
for i in arr:
    add_arr += i
answer = 0
a, b = map(int, input().split())
for j in add_arr[a-1:b]:
    answer += int(j)

print(answer, len(add_arr))