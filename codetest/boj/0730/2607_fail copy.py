n = int(input())
arr = []
for i in range(n):
    word = input()
    li = {}
    for j in word:
        if j not in li:
            li[j] = 0
        if j in li:
            li[j] += 1
    arr.append(li)

stan = arr[0]
cnt = 0
for k in arr[1:]:
    if k == stan:
        cnt += 1
print(cnt)

# 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우 비슷
