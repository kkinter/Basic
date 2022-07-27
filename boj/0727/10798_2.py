
arr = []
length = []
for _ in range(5):
    word = input()
    arr.append(word)
    length.append(len(word))

res = ''

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            res += arr[j][i]

print(res)