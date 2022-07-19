t = int(input())

for i in range(t):
    s = input()
    if s == s[::-1]:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")
    print(s,s[::-1])
