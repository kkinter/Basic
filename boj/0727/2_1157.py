word = input().lower() # 대소문자를 가리지 않기 때문에, 입력에서 소문자로 변환
li = {}
for i in word:  # 입력의 문자열의 요소 중에서 
    if i not in li:
        li[i] = 0
    if i in li:
        li[i] += 1
res = []
for key, value in li.items():
    if value == max(li.values()):
        res.append(key)

if len(res) == 1:
    print("".join(res).upper())
else:
    print("?")
