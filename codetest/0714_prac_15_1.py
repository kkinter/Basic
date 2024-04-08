s = input()
cnt = 0
if 'a' in s:
    for i in range(len(s)):
        if s[i] == 'a':
            print(i)
            break
else:
    print(0)    
