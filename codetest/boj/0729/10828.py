# 시간 초과
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    command = input().split()
    length = len(arr)
    # 정수 x를 스택에 넣는 연산
    if len(command) == 2:
        arr.append(command[1])
    else:
        
        if command == ['pop']:
            # 스택의 위에 있는 정수를 뺴고, 그 수를 출력
            if length >= 1:
                print(arr[-1])
                arr.pop(-1)
            # 비어있다면 -1 출력    
            else:
                print(-1)
        # 스택에 들어 있는 정수의 개수를 출력
        elif command == ['size']:
            print(length)
        # 스택이 비어있으면 1, 아니면 0
        elif command == ['empty']:
            if length == 0:
                print(1)
            else:
                print(0)
        elif command == ['top']:
            if length == 0:
                print(-1)
            else:
                print(arr[-1])