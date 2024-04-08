import sys
input = sys.stdin.readline
n = input()
def foo(n, cnt):
    sum_val = 0
    
    for i in n:
        sum_val += int(i)
    
    if n == '1':
        print(cnt)
        print('NO')
        return
    
    elif sum_val % 3 == 0:
        cnt += 1
        print(cnt)
        print('YES')
        return

    elif sum_val % 3 != 0:
        cnt += 1
        foo(sum_val, cnt)
        
foo(n, 0)
