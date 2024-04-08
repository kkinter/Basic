s = input()

# li = []
# for i in s:
#     if i not in li:
#         li.append(i)
# print(li)

li = set()
for i in s:
    li.add(i)
print(li)

dict_1 = {}
for i in li:
    dict_1[i] = 0
print(dict_1)

for i in s:
    for j in dict_1:
        if j == i:
            dict_1[j] += 1

print(dict_1)
