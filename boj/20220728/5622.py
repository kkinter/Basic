##  2 : A, B, C 는 3초 
##  9 : W, X, Y, Z 는 10초
cnt = 0
word = input()
for i in word:
    if i in 'ABC':
        cnt += 3
    if i in 'DEF':
        cnt += 4
    if i in 'GHI':
        cnt += 5
    if i in 'JKL':
        cnt += 6
    if i in 'MNO':
        cnt += 7
    if i in 'PQRS':
        cnt += 8
    if i in 'TUV':
        cnt += 9
    if i in 'WXYZ':
        cnt += 10

print(cnt)