import sys
sys.stdin = open("./4949.txt")
input = sys.stdin.readline
arr = []

while True:
    word = input().strip()
    if word == '.':
        arr.append(word)
        break
    arr.append(word)



for j in arr:
    stk = []
    stk_2 = []
    for k in j:
        is_val = True
        if k == '(':
            stk.append(k)
        elif k == ')':
            if len(stk) > 0:
                stk.pop()
            else:
                is_val = False
                print('괄호 초과')
                break
        
        if k == '[':
            stk_2.append(k)
        elif k == ']':
            if len(stk_2) > 0:
                stk_2.pop()
            else:
                is_val = False
                print('대괄호 초과')
                break

        print(stk, stk_2)


    if len(stk) > 0 or len(stk_2) > 0:
        is_val = False
    
    print(stk, stk_2, is_val)

