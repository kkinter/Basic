T = int(input()) #3

for test_case in range(1, T + 1):
    a,b = map(int,input().split())
    print(test_case)
    print(f"#{test_case} {a//b} {a%b}")
