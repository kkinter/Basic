# import sys
# # sys.stdin = open("./4949.txt")
# input = sys.stdin.readline

while True:
    word = input()
    stk = []
    
    if word == '.':
        break

    for k in word:
        if k == '[' or k == '(':
            stk.append(k)

        elif k == ']':
            if len(stk) > 0 and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(k)
                break            

        elif k == ')':
            if len(stk) > 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(k)
                break
            

    if len(stk) == 0:
        print('yes')
    else:
        print('no')
    

