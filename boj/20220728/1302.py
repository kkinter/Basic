n = int(input())
dict = {}
for i in range(n):
    book = input()
    if book not in dict:
        dict[book] = 0
    if book in dict:
        dict[book] += 1


max_dict = max(dict.values())

res = [] # value 가 최대인 key 값을 저장하기 위한 리스트 생성
for key, value in dict.items():
    if dict[key] == max_dict: # 밸류값이 max 면 리스트에 저장
        res.append(key)
print(sorted(res)[0]) # 리스트의 요소 중 key 값이 최소인 요소 출력