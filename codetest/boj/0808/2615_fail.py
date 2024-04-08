import sys
from pprint import pprint

sys.stdin = open('./2615.txt')
matrix = [list(map(int, input().split())) for _ in range(19)]


delta = [[(1 , 1), (2 , 2), (3 , 3), (4 , 4)], [(1 , 0), (2 , 0), (3 , 0), (4 , 0)], [(0 , 1), (0 , 2), (0 , 3), (0 , 4)], [(-1, 1), (-2, 2), (-3, 3), (-4, 4)]]
six_check = [(5, 5),(5, 0), (0, 5), (-5, 5)]
# 6개인 경우를 어떻게 잡아내야하누
is_win = False
for i in range(19):
    for j in range(19):
        if matrix[i][j] == 1 or matrix[i][j] == 2:
            cnt_arr = [0, 0, 0, 0]
            for d in range(4):
                for dir in delta[d]:
            
                    try:
                        nx = j + dir[1]
                        ny = i + dir[0]
                        if matrix[i][j] == matrix[ny][nx]:
                            cnt_arr[d] += 1
                        
                        if cnt_arr[d] == 4:
                            try:
                                if matrix[i + six_check[d][0]][j + six_check[d][1]] != matrix[i][j]:
                                    break
                            except:
                                pass

                            try:
                                if matrix[i - delta[d][0][0]][j - delta[d][0][1]] != matrix[i][j]:
                            except:
                                pass

                            is_win = True
                            print(matrix[i][j])
                            # print(matrix[i + six_check[d][0]][j + six_check[d][1]])
                            # print(matrix[i - delta[d][0][0]][j - delta[d][0][1]])
                            print(i + 1, j + 1)
                    except:
                        # print(f'{nx} {ny} 오류')
                        pass
if not is_win:
    print(0)
            
