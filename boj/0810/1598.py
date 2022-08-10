a, b = map(int, input().split())
a = a - 1
b = b - 1
wid = abs((b // 4)  - (a // 4))
hei = abs((b % 4)  - (a % 4))
print(wid + hei)