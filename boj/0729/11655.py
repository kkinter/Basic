def rot13(str):
    new = ''
    for i in str:
        if i.isalpha() == False:
            new += i
        elif i >= 'A' and i <= 'M':
            new += chr(ord(i) + 13)
        elif i >= 'N' and i <= 'Z':
            new += chr(ord(i) - 13)
        elif i >= 'a' and i <= 'm':
            new += chr(ord(i) + 13)
        elif i >= 'n' and i <= 'z':
            new += chr(ord(i) - 13) 
    return new

s = input()
print(rot13(s))