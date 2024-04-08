n = int(input())
res = 0
for i in range(4, n + 1):
    if str(i).count('4') + str(i).count('7') == len(str(i)):
        res = max(res, i)

print(res)
