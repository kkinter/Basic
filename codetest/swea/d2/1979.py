import sys
sys.stdin = open('./1979.txt')


t = int(input())
for q in range(t):
    n, k = map(int, input().split())
    matrix = [list(map(str, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        row = ''
        col = ''
        
        for j in range(n):
            row += matrix[i][j]
        row = row.split('0')
        for l in row:
            if len(l) == k:
                cnt += 1
        
        for j in range(n):
            col += matrix[j][i]
        col = col.split('0')
        for l in col:
            if len(l) == k:
                cnt += 1

    print(f'#{q + 1} {cnt}')

    
    


    