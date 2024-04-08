
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

rank_rev = sorted(li_rank, reverse=True)

for j in range(-1,-n - 1,-1):  # 4, 3, 2 ,1
    for k in rank_rev: # 0, 1, 2, 3
        
        # if li_rank[j] < li_rank[k] and li_weight[j] < li_weight[k]:
        #     li_rank[k] = li_rank[j]

print(" ".join(map(str, li_rank)).rstrip())