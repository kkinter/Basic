ulim = list(map(int, input().split()))
link = list(map(int, input().split()))

score = []
is_win = False
for i in range(len(ulim)):
    diff = ulim[i] - link[i]
    score.append(diff)
    if score[-1] > 0:
        is_win = True
    elif sum(score[:-1]) == 0 and ulim[i] > 0:
        is_win = True

if is_win:
    print('Yes')
else:
    print('No')