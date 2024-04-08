
s = input()

for i in s:
    if i.isalpha() == True:
        if ord(i) > 96:
            print(chr(ord(i)-32),end='')
        else:
            print(i,end='')
    else:
        print(i,end='')