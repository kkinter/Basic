
n = int(input())
li = []
for i in range(n):
    li.append(list(map(str, input().split())))

name = [x[0] for x in li]
year = [x[3] for x in li]
mon = [x[2] for x in li]
day = [x[1] for x in li]

day_sum = [(int(year[i])*365 + int(mon[i])*30 + int(day[i])) for i in range(n)]

young = day_sum.index(max(day_sum))
old = day_sum.index(min(day_sum))

print(name[young])
print(name[old])