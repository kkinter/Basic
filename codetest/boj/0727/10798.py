
arr = []
for i in range(5):
    s = input()
    arr.append([x for x in s])
dx = 0
dy = 0
string = ''
while True:
    try:
        string += arr[dx][dy]   
    except:
        dx += 1
    if dx == len(arr) - 1:
        dy += 1
        if dy == len(arr[dx]):
            break
        dx = 0
    else:
        print('인덱스 초과')
        dx += 1
        
    
print(string.rstrip())

# Aa0aPAf985Bz1EhCz2W3D1gkD6x
# Aa0aPAf985Bz1EhCz2W3D1gkD6x