t = int(input())
for i in range(t):
    n = int(input())
    string = ''
    for j in range(n):
        c, k = input().split()
        string += c*int(k)

    cnt = 10
    print(f"#{i+1}")
    for s in string:
        if cnt != 1:
            print(s, end='')
            cnt -= 1
        else:
            print(s, end='\n')
            cnt = 10
    print("")            

