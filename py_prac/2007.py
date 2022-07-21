t = int(input())

for i in range(t):
    s= input()
    cnt = 0
    word = s[0]
    strat = s[0]
    for i in range(1,29):
        if s[i] == s[0] and s[i+1] == s[1]:
            break
        else:
            word += s[i]
    print(f"#{i+1} {len(word)}")             
    # while len(s) > len(word):
    #     if word in s:
    #         s = s.replace(word,'',1)
    #         cnt +=1
        
    # print(f"#{i+1} {cnt}")
