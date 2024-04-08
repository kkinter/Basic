n = input()
dict = {'c=': 1, 'c-': 1, 'dz=': 1, 'd-': 1, 'lj': 1, 'nj': 1, 's=': 1, 'z=': 1}
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
# while len(n) > 0:
#     for i in li:
#         print(i, n)
#         if i in n:
#             n.replace(i,'')
#             cnt += len(i)

## str += 활용했을 때
# new_ = ''
# for i in n:
#     new_ += i
#     cnt += 1
#     print(new_)
#     if new_ in dict.keys():
#         cnt -= len(new_)
#         cnt += dict.get(new_)
#         new_ = ''
# print(cnt)
cnt = 0
cnt += len(n)
res = ''
res += n
for i in dict.keys():
    while i in res:
        res = res.replace(i, " ", 1)
        if len(i) == 2:
            cnt -= 1
        if len(i) == 3:
            cnt -= 2
print(cnt)

