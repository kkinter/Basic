
c, k = input().split()
str = ''
str += c*int(k)
cnt = 10
for s in str:
    if cnt != 1:
        print(s, end='')
        cnt -= 1
    else:
        print(s, end='\n')
        cnt = 10
        
