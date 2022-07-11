a, b, c= map(int,input().split())

li = [a,b,c]
for i in li:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')    