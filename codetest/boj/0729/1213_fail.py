# word = input()
word = 'aaabb'
dic = {}
for i in word:
    if i not in dic:
        dic[i] = 0
    if i in dic:
        dic[i] += 1
# 팰린드롬 조건  > 각 key 의 밸류값과 key 개수가 2보다 크면 V
# key 개수가 1개이면, 다른 밸류값과 key 개수가 동일해야한다
# 그냥 완전 탐색 
# 그냥 4개의 원소로 만들수 있는 배열의 집합


print(word, dic)
res = []
for j in range(len(word)):
    new = ''    
    for k in range(len(word)):
        if k != j:
            new += word[k]
            
    new_list = new.split()
    new_list.insert(j, word[j])
    final = "".join(new_list)

    res.append(final)

print(res)