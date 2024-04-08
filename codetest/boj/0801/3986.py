from operator import le


n = int(input())
stk = []
is_a = False
is_b = False

for i in range(n):
    word = input()
    for j in word:
        if j == 'A':
            if is_b != False:
                break
            else:
                is_a = True
        elif j == 'B':
            
        
            
        

