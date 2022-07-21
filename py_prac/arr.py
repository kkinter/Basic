li = [15, 20, 8, 28, 16, 27, 17, 27, 10, 12]
n = len(li)
for j in range(n-1):
    for i in range(n-j-1):
        if li[i] > li[i +1]:
            li[i], li[i+1] = li[i+1], li[i]
print(li)