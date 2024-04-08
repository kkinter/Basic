import sys
sys.stdin = open('./1063.txt')
alpha = 'ABCDEFGH'
direction = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1) }
coor = {}
cnt = 1
for i in alpha:
    coor[i] = cnt
    cnt += 1

k, s, n = map(str, input().split())
k = list(k)
king = [coor[k[0]], int(k[1])]
s = list(s)
stone = [coor[s[0]], int(s[1])]

for j in range(int(n)):
    move = input()
    if move in direction:
        if 1 <= king[0] + direction[move][0] < 9 and 1 <= king[1] + direction[move][1] < 9:
            king[0] += direction[move][0]
            king[1] += direction[move][1]
            if king[0] == stone[0] and king[1] == stone[1]:
                if 1 <= stone[0] + direction[move][0] < 9 and 1 <= king[1] + direction[move][1] < 9:
                    stone[0] += direction[move][0]
                    stone[1] += direction[move][1]
                else:
                    king[0] -= direction[move][0]
                    king[1] -= direction[move][1]
    
res_king = ''
res_stone = ''
for key, val in coor.items():
    if king[0] == val:
        res_king = key + str(king[1])
    if stone[0] == val:
        res_stone = key + str(stone[1])
print(res_king)
print(res_stone)
