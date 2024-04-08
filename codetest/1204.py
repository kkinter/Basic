t =int(input())
for i in range(1,t+1):
    a = int(input())
    li = list(map(int,input().split()))
    dict = {}
    for i in li:
        if i not in dict:
            dict[i] = 0
        if i in dict:
            dict[i] += 1
    max_val = max( dict , key = dict.get)
    print(f"#{a} {max_val}")