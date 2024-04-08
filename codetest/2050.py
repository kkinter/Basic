s = input()

for i in s:
    if i != s[-1]:
        print(ord(i)-64,end=' ')
    else:
        print(ord(i)-64,end='')