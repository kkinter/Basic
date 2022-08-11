n = int(input())
for i in range(n):
    a, b = input().split()
    hash = {}
    hash2 = {}
    for i in a:
        if i not in hash:
            hash[i] = 0
        if i in hash:
            hash[i] += 1
    
    for j in b:
        if j not in hash2:
            hash2[j] = 0
        if j in hash2:
            hash2[j] += 1
    if hash == hash2:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')