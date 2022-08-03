n = int(input())
arr = []
for i in range(n):
    word = input()
    li = set()
    for j in word:
        li.add(j)
    arr.append(li)

stan = arr[0]
cnt = 0
for k in arr[1:]:
    if k == stan:
        cnt += 1
print(cnt)

# 접근 방법이 잘못된듯
# 문제를 제대로 안읽음
