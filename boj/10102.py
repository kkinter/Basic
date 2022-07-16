v = int(input())
s = input()
acnt = 0
bcnt = 0
for i in s:
    if i == 'A':
        acnt += 1
    elif i == 'B':
        bcnt += 1

if acnt > bcnt :
    print('A')
elif acnt == bcnt :
    print('Tie')
else:
    print('B')