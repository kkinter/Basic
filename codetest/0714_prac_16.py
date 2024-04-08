s = input()
li = ['a','e','i','o','u']
cnt = 0

for i in s:
    for j in li:
        if j == i:
            cnt += 1

print(cnt)