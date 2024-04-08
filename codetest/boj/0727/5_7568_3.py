

n = int(input())
li_weight = []
li_height = []
for i in range(n):
    weight, height = map(int, input().split())
    li_weight.append(weight)
    li_height.append(height)
rank_w = []
rank_h = []


for h in li_height:
    cnt = 1
    for hh in li_height:
        if h < hh:
            cnt +=1
    rank_h.append(cnt)
res = []
print(rank_h)

for w in li_weight:
    cnt = 1
    for ww in li_weight:
        if w < ww:
            cnt +=1
    rank_w.append(cnt)

print(rank_w)


for r in range(n):
    res.append(min(rank_w[r], rank_h[r]))

print(res)
            

