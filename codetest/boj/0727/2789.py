s = input()
res = ''
for i in s:
    if i not in 'CAMBRIDGE':
        res += i

print(res)