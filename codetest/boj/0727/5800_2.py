n = int(input())
for i in range(n):
    gap = 0
    li = list(map(int, input().split()))
    rev_li = sorted(li[1:], reverse= True)
    for k in range(1, len(li) - 2):
        gap = max(gap, (rev_li[k] - rev_li[k + 1]))
    print(f"Class {i + 1} ")
    print(f"Max {max(li[1:])}, Min {min(li[1:])}, Largest gap {gap}")

# for j in range(n):
#     print(f"Max {max_ans[j]}, Min {min_ans[j]}, Largest gap {max_gap[j]}")