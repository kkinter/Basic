li = [185, 183, 186, 175, 155]
li_rev = sorted(li,reverse= True)# [186, 185, 183, 175, 155]
li_rank = []
for i in li:
    li_rank.append(li_rev.index(i) + 1)
print(li_rank)