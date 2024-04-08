a_card = list(map(int, input().split()))
b_card = list(map(int, input().split()))
a_cnt = 0
b_cnt = 0
d_cnt = 0
lst_win = ''

for i in range(10):
    if a_card[i] > b_card[i]:
        a_cnt += 3
        lst_win = 'A'
    elif b_card[i] > a_card[i]:
        b_cnt += 3
        lst_win = 'B'
    elif a_card[i] == b_card[i]:
        a_cnt += 1
        b_cnt += 1
        d_cnt += 1
    

if d_cnt == 10:
    lst_win = 'D'

print(a_cnt, b_cnt)
if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
elif a_cnt == b_cnt:
    print(lst_win)