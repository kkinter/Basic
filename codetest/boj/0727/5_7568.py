
n = int(input())
compare = []
for i in range(n):
    li = list(map(int, input().split()))
    compare.append(li)

temp = []
# 순위 정렬
li_height = [i[1] for i in compare]
li_weight = [i[0] for i in compare]

li_rev = sorted(li_height,reverse= True) # [186, 185, 183, 175, 155]
li_rank = []
for i in li_height:
    li_rank.append(li_rev.index(i) + 1)

for j in range(n):
    for k in range(n):
        if li_rank[j] < li_rank[k] and li_weight[j] < li_weight[k]:
            li_rank[k] = li_rank[j]

print(" ".join(map(str, li_rank)).rstrip())