n = int(input())
max_ans = []
min_ans = []
max_gap = []
for i in range(n):
    gap = 0
    li = list(map(int, input().split()))
    max_ans.append(max(li[1:]))
    min_ans.append(min(li[1:]))
    rev_li = sorted(li[1:], reverse= True)
    for k in range(1, len(li) - 2):
        gap = max(gap, (rev_li[k] - rev_li[k + 1]))
    max_gap.append(gap)

for j in range(n):
    print(f"Class {j + 1}")
    print(f"Max {max_ans[j]}, Min {min_ans[j]}, Largest gap {max_gap[j]}")

# Max 99, Min 25, Largest gap 25
# Max 99, Min 25, Largest gap 25