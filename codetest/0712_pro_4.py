from unittest import result


n = int(input())
cnt = 1
results = 1

# while cnt <= n:
#     results *= cnt
#     cnt += 1

# print(results)

for i in range(1,n+1):
    results *= i
print(results)