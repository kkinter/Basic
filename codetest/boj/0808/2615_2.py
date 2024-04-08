import sys
from pprint import pprint

sys.stdin = open('./2615.txt')
matrix = [list(map(int, input().split())) for _ in range(19)]


delta = [(1 , 1), (1 , 0), (0 , 1), (-1, 1)]

# 6개인 경우를 어떻게 잡아내야하누
is_win = False
for i in range(19):
    for j in range(19):
        if matrix[i][j] == 1 or matrix[i][j] == 2:
            cnt_arr = [0, 0, 0, 0]
            nx = j
            ny = i
            for d in range(4):
                for _ in range(5):
                    try:
                        nx = nx + delta[d][1]
                        ny = ny + delta[d][0]
                        
                        if matrix[i][j] == matrix[ny][nx]:
                            cnt_arr[d] += 1
                        if cnt_arr[d] == 4:
                            print(1, i, j)
                    except:
                        pass
            print(cnt_arr)


                    
# if not is_win:
#     print(0)
            
