w = sorted([int(input()) for _ in range(10)], reverse= True)
k = sorted([int(input()) for _ in range(10)], reverse= True)

print(sum(w[0:3]), sum(k[0:3]))