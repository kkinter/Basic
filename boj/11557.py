for _ in range(int(input())):
    dict = {}
    li = []
    for i in range(int(input())):
        name, vol = input().split()
        dict[name] = int(vol)
    # li.append(max(dict, key=dict.get))
    print(max(dict, key=dict.get))
# for i in li:
#     print(i)
